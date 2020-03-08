from model.ProjectPOI import ProjectPOI, FunctionD
from controllers.DataService import createProjectPOI

class POI:
    def __init__(self, name):
        self.content = dict()
        self.content['name'] = name
        self.content['r2name'] = name
        self.check = True

    def getContent(self):
        return self.content

class String(POI):
    def __init__(self, name):
        super().__init__(name)
        self.content['size'] = None
        self.content['call'] = None

    def getInfo(self):
        infoDict = dict()
        for content in self.content:
            infoDict[content] = str(self.content[content])
        return infoDict

    def toProjectPoi(self):
        return createProjectPOI("string", self.content['name'],self.content['r2name'],None,self.check)

    def importFromDatabase(self, projectPOI):
        self.content['name'] = projectPOI.name
        self.content['calls'] = projectPOI.calls

class Var(POI):
    def __init__(self, name=None, type=None):
        super().__init__(name)
        self.content['type'] = type
        self.content['value'] = []

    def getInfo(self, indent):
        infoDict = dict()
        if self.content['name'] is not None:
            infoDict['name'] = self.content['name']
        infoDict['type'] = self.content['type']
        if 'call' in self.content.keys():
            infoDict['call'] = self.content['call']
        infoDict['value'] = self.content['value']
        return infoDict

    def toProjectPOI(self):
        return createProjectPOI(self.content['type'], self.content['name'],self.content['r2name'],self.content['value'],self.check)

    def importFromDatabase(self, projectPOI):
        self.content['name'] = projectPOI.name
        self.content['r2name'] = projectPOI.r2Name
        self.content['type'] = projectPOI.type
        self.content['parameters'] = projectPOI.data
        self.content['calls'] = projectPOI.calls

class Function(POI):
    def __init__(self, name):
        super().__init__(name)
        self.content['calls'] = []
        self.content['parameters'] = []
        self.content['return'] = None

    def addCall(self, call):
        self.content['calls'].append(call)

    def addParam(self, param):
        self.content['params'].append(param)

    def getInfo(self):
        infoDict = dict()
        parameters = list()
        infoDict['name'] = str(self.content['name'])
        infoDict['calls'] = self.content['calls']
        infoDict['return'] = self.content['return']
        if len(self.content['parameters']) is 0:
            infoDict['parameters'] = "None"
        for var in self.content['parameters']:
            parameters.append(var.getInfo(''))
        infoDict['parameters'] = parameters
        infoDict['return'] = [self.content['return'].getInfo('')]
        return infoDict

    def toProjectPoi(self):
        vars = [var.toProjectPOI() for var in self.content['parameters']]
        projectPOI = createProjectPOI("function",self.content['name'],self.content['r2name'],vars,self.check)
        projectPOI.calls = self.content['calls']
        projectPOI.returnV = self.content['return'].toProjectPOI()
        return projectPOI

    def importFromDatabase(self, functionD):
        self.content['name'] = functionD.name
        self.content['r2name'] = functionD.r2Name
        self.content['parameters'] = functionD.data
        self.content['calls'] = functionD.calls
        self.content['comment'] = functionD.comment
        self.check = functionD.check
        self.content['return'] = functionD.returnV

    def split_function_call(self):
        if len(self.content['calls']) <= 1:
            return [self]
        functions = []
        for call in self.content['calls']:
            func = Function(self.content['r2name'])
            func.content = self.content.copy()
            func.content['calls'] = [call]
            func.content['name'] = self.content['r2name'] + " @ " + call
        return functions

def import_ProjectPOI(ppoi):
    poi = None
    if ppoi.type == 'String':
        poi = String(ppoi.name)
        poi.content['calls'] = ppoi.calls
        poi.content['r2Name'] = ppoi.r2Name
    if ppoi.type == 'Function':
        poi = Function(ppoi.name)
        poi.content['calls'] = ppoi.calls
        for d in ppoi.data:
            poi.content['parameters'].append(import_ProjectPOI(d))
        poi.content['r2Name'] = ppoi.r2Name
        poi.content['return'] = ppoi.size_return
    return poi
