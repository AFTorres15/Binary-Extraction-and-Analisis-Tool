import r2pipe, sys, os, json, io
from PyQt5 import QtCore
from contextlib import redirect_stdout


class Dynamic(QtCore.QThread):
    message = QtCore.pyqtSignal(str)
    finished = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(Dynamic, self).__init__(parent)
        self.runningD = False
        self.started = False
        self.content = dict()
        self.r2 = None
        self.args = ""

    def getFunctionNames(self):
        temp = [a.content['name'] for a in self.content['Function']]
        return temp

    def import_static(self, content):
        self.r2 = content[0]
        self.content = content[1]

    def stop(self):
        self.runningD = False

    def run(self):
        self.runningD = True
        #self.r2._cmd_pipe = self
        sys.stdout = self

        print("Starting Dynamic")
        # hardcoded run
        self.r2.cmd('doo ' + self.args)
        #self.r2.cmd('of ' + str(json.loads(self.r2.cmd('oj'))[0]['fd']))

        print("Setting Breakpoints")
        for func in self.content['Function']:
            if func.check:
                for call in func.content['calls']:
                    print("Breakpoint: " + str(call))
                    self.r2.cmd('db ' + str(call))
                    #self.r2.cmd('db @' + str(call))
        print("Breakpoints Set")

        i=0
        while len(json.loads(self.r2.cmd("dpj"))) > 1:
            if i % 2 != 0:
                self.r2.cmd('dc')
            else:
                self.r2.cmd('dso')

            address = self.r2.cmd('s').replace('\n','')
            self.call_to_function(address)
            i+=1
        print('Stopped')
        self.finished.emit()

    def call_to_function(self, address):
        #This line is used for hex math
        #add = int(address.replace('\n',''),16) - int('0x400000',16)
        for function in self.content['Function']:
            for function_call in function.content['calls']:
                if function_call == address:
                    print("Data found for function: " + function.content['r2name'])
                    for parameter in function.content['parameters']:
                        print(parameter.content['type'])
                        param_name = parameter.content['r2name']
                        if param_name.__contains__('rbp') or param_name[0] == 'r':
                            payload = self.r2.cmdj('pxj @ ' + param_name)
                            parameter.content['value'].append(payload)
                        else:
                            payload = self.r2.cmd('dr ' + param_name)
                            payload = str(payload).replace('\n','')
                            parameter.content['value'].append(payload)
                    break

    def write(self, msg):
        self.message.emit(msg)
