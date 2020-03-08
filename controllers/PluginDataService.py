from model.PluginData import PluginData
from model.PluginPOI import PluginPOI

#saves new plugins
def createPlugin(path: str, pds:str, name: str, desc: str, poi: list):
    plugin = PluginData()
    plugin.name = name
    plugin.predefinedDataSet=pds
    plugin.description = desc
    plugin.path = path
    plugin.pluginPOI = poi
    plugin.save()

#Returns a plugin by it's name
def getPlugin(name: str):
    plugin = PluginData.objects(name=name).first()
    return plugin

def getAllPlugins():
    allPlugins = PluginData.objects

    pluginNames = []
    for plugin in allPlugins:
        pluginNames.append(plugin.name)

    return pluginNames

# Deletes a project document
def deletePlugin(name):
    project = getPlugin(name)
    project.delete()

# Updates a project's info by its name
def updatePlugin(currentName: str, newName: str, desc: str):
    plugin = getPlugin(currentName)
    PluginData.objects(id=plugin.id).update_one(set__description=desc, set__name=newName)
    plugin = getPlugin(newName)

    return plugin.name

def getPOI(pluginName: str, poi_name: str):
    plugin = getPlugin(pluginName)
    pois = plugin.pluginPOI

    for poi in pois:
        if poi.name == poi_name:
            return poi

def getPluginPOI(pluginName: str):
    plugin = PluginData.objects(name=pluginName).first()

    allPOI = plugin.pluginPOI
    pois = []
    for poi in allPOI:
        pois.append(poi)

    return pois

def getPluginPOINames(pluginName: str):
    plugin = PluginData.objects(name=pluginName).first()

    allPOI = plugin.pluginPOI
    poiNames = []
    for poi in allPOI:
        poiNames.append(poi.name)

    return poiNames

def getPluginPOITypes(pluginName: str):
    plugin = PluginData.objects(name=pluginName).first()

    allPOI = plugin.pluginPOI
    poiNames = []
    for poi in allPOI:
        poiNames.append(poi.type)

    return set(poiNames)

def getPOIFromType(pluginName: str, type: str):
    plugin = getPlugin(pluginName)
    pois = plugin.pluginPOI

    filteredPOI = []
    for poi in pois:
        if poi.type == type:
            filteredPOI.append(poi.name)
    return filteredPOI


#Adds POI to plugin using plugin's name
def addToPlugin(name:str, poi:PluginPOI ):
    plugin = PluginData.objects(name=name).first()
    plugin.pluginPOI.append(poi)
    plugin.save()

def createPOI(name: str, type: str, return_type: str, data: dict):
    poi = PluginPOI()
    poi.name = name
    poi.type = type
    poi.size_return = return_type
    poi.data = data

    return poi

def insertNewPOIToPlugin(pluginName: str, poiName: str, type: str, return_type: str, data: dict):
    addToPlugin(pluginName, createPOI(poiName, type, return_type, data))

#creates POI's for the plugin
def createPluginPOI(path: str, pds:str, name: str, desc: str, poi: list):
    plugin = PluginData()
    plugin.name = name
    plugin.predefinedDataSet=pds
    plugin.description = desc
    plugin.path = path
    plugin.pluginPOI = poi
    plugin.save()

def deletePOI(pluginName: str, poiName: str):
    plugin = PluginData.objects(name=pluginName).first()

    pois = plugin.pluginPOI

    for poi in pois:
        if poi.name == poiName:
            plugin.pluginPOI.remove(poi)
            plugin.save()
            return

def updatePOI(pluginName: str, poiName: str, newPOIName: str, type: str, return_type: str, data: dict):
    plugin = PluginData.objects(name=pluginName).first()

    pois = plugin.pluginPOI

    for i, poi in enumerate(pois):
        if poi.name == poiName:
            plugin.pluginPOI[i] = createPOI(newPOIName, type, return_type, data)
            plugin.save()
            return newPOIName
