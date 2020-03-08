import mongoengine
import r2pipe,json,sys
from PyQt5 import QtCore
from model.ProjectPOI import ProjectPOI, FunctionD
from model.POI import Function, Var, String, POI

class Static(QtCore.QThread):
    message = QtCore.pyqtSignal(str)
    poi_name = QtCore.pyqtSignal(str)
    finished = QtCore.pyqtSignal()
    add_poi = QtCore.pyqtSignal(ProjectPOI)
    add_function = QtCore.pyqtSignal(FunctionD)

    def __init__(self, filePath, plugin_pois):
        super(Static, self).__init__()
        self.setPluginData(plugin_pois)
        self.filePath = filePath

        self.r2 = r2pipe.open("server.out")
        sys.stdout = self
        self.content = dict()
        self.content['Function'] = []
        self.content['String'] = []

    def run(self):
        self._openFile()
        self._r2Analyze()
        self._findFunctions()
        self._findString()
        self.finished.emit()

    def getContent(self):
        return self.r2, self.content

    def getPOINames(self):
        names = self.getFunctionNames()
        names += self.getStringNames()
        return names

    def getStringNames(self):
        names = [a.content['name'] for a in self.content['String']]
        return names

    def getFunctionNames(self):
        names = [a.content['name'] for a in self.content['Function']]
        return names

    def getPOI(self, name):
        i = 0
        for function in self.content['Function']:
            if function.content['name'] == name:
                i+=1
            if function.content['name'] == name:
                return function
        for string in self.content['String']:
            if string.content['name'] == name:
                i+=1
            if string.content['name'] == name:
                return string
        return i

    def _r2Analyze(self):
        print("Analysing")
        self.r2.cmd('aaa')

    def _openFile(self):
        self.r2.cmd('o ' + self.filePath)
        self.r2.cmd('o-!*')
        print("Success")

    def _findString(self):
        print("Gathering Strings")
        r2String = json.loads(self.r2.cmd('fs strings;fj'))
        for r2String in r2String:
            plugin_poi = None
            for pp in self.plugin_pois['String']:
                if r2String['realname'].__contains__(pp['name']):
                    plugin_poi =  pp
                    break
            if plugin_poi is None:
                continue

            string = String(r2String['realname'])
            string.content['size'] = r2String['size']
            string.content['call'] = hex(r2String['offset'])
            self.poi_name.emit(string.content['name'])
            self.content['String'].append(string)

            self.poi_name.emit(string.content['name'])
            self.content['String'].append(string)
            self.add_poi.emit(string.toProjectPoi())


    def _findFunctions(self):
        print("Gathering Functions")
        r2Functions = json.loads(self.r2.cmd('aflj'))
        for r2Function in r2Functions:
            if r2Function['name'] in self.getFunctionNames():
                pass
            plugin_poi = None
            for pp in self.plugin_pois['Function']:
                if r2Function['name'].__contains__(pp['name']):
                    plugin_poi =  pp
                    break
            if plugin_poi is None:
                continue
            function = Function(r2Function['name'])
            #function.content = r2Function

            '''
            #Handle Stack Vars
            self.r2.cmd('s ' + function.content['name'])
            vars = json.loads(self.r2.cmd('afvbj'))
            for bp in vars:
                _var = Var(bp['ref']['base'] + " " + str(bp['ref']['offset']), bp['type'])
                function.content['parameters'].append(_var)
            # Handle Register Variables
            link = []
            vars = json.loads(self.r2.cmd('afvrj'))
            for bp in vars:
                _var = Var(bp['ref'], bp['type'])
                function.content['parameters'].append(_var)
            '''
            total_vars = len(plugin_poi['data'])
            vars_count = 0
            var_types = list(plugin_poi['data'].values())
            var_names = list(plugin_poi['data'].keys())

            r2GetCalls = 'axtj @ ' + function.content['name']
            for ref in json.loads(self.r2.cmd(r2GetCalls)):
                if ref['type'] == 'CALL':
                    function.addCall(str(hex(ref['from'])))
                    self.r2.cmd('s ' + str(hex(ref['from'])))
                    i=0
                    while total_vars > vars_count:
                        i+=1
                        code = json.loads(self.r2.cmd('pdj ' + str(-i)))
                        if code[0]['type'] == 'mov' or code[0]['type'] == 'lea':
                            split_cmd = code[0]['opcode'].replace(',','').split()
                            if split_cmd[1] == 'qword':
                                _var = Var(" ".join(split_cmd[2:-1]).replace('[','').replace(']',''), var_types[vars_count])
                                _var.content['name'] = var_names[vars_count]
                            elif split_cmd[1].__contains__("word"):
                                pass
                            elif split_cmd.__contains__("rsi"):
                                break
                            else:
                                _var = Var(split_cmd[1], var_types[vars_count])
                                _var.content['name'] = var_names[vars_count]
                            function.content['parameters'].append(_var)
                            vars_count+=1
                        else:
                            break

            if(len(function.content['calls']) <= 0) or (total_vars != vars_count):
                continue

            function.content['name'] += " @ " + str(function.content['calls'])
            _var = Var("rsi", plugin_poi['size_return'])
            _var.content['name'] = None
            function.content['return'] = _var

            for function_call in function.split_function_call():
                self.poi_name.emit(function_call.content['name'])
                self.content['Function'].append(function_call)
                self.add_function.emit(function_call.toProjectPoi())

    def getFileInfo(self):
        r2GetInfo = '!rabin2 -Ij ' + self.filePath
        r2FileInfo = json.loads(self.r2.cmd(r2GetInfo))['info']
        fileInfo = []
        fileInfo.append(r2FileInfo['os'])
        fileInfo.append(r2FileInfo['bintype'])
        fileInfo.append(r2FileInfo['machine'])
        fileInfo.append(r2FileInfo['class'])
        fileInfo.append(r2FileInfo['bits'])
        fileInfo.append(r2FileInfo['lang'])
        fileInfo.append(r2FileInfo['canary'])
        fileInfo.append(r2FileInfo['crypto'])
        fileInfo.append(r2FileInfo['nx'])
        fileInfo.append(r2FileInfo['pic'])
        fileInfo.append(r2FileInfo['relocs'])
        fileInfo.append(r2FileInfo['stripped'])
        return fileInfo

    def write(self, msg):
        self.message.emit(msg)

    def setPluginData(self, plugin_pois):
        self.plugin_pois = plugin_pois

def decypher(messageArr):
    byteStr = ""
    for i in range(len(messageArr)):

        # If found 0 byte...then is end of message in memory.
        if messageArr[i] == 0:
            break
        # building byte string.
        byteStr = byteStr + str(hex(messageArr[i]))[2:] + " "

    return byteStr
