from lxml import etree
from lxml.etree import tostring
from lxml.builder import E

class PluginXMLHandler(object):

    # get all the plugin names
    def loadPlugins(self):
        root = etree.parse("temp/Plugins.xml").getroot()

        plugins = []
        for name in root.iter('name'):
            if name.getparent().tag == 'plugin':
                plugins.append(name.text)

        return plugins

    # get all attributes of a plugin
    def getPluginInfo(self, pluginName):
        root = etree.parse("temp/Plugins.xml")
        path = root.xpath('plugin[name="%s"]' % pluginName)

        attributes = []
        for plugin in path:
            attributes.append(plugin.find('description').text)
            attributes.append(self.getPOI(pluginName))
            attributes.append(self.getOutput(pluginName))

        return attributes

    # get all name of poi associated with a plugin
    def getPOI(self, pluginName):
        root = etree.parse('temp/Plugins.xml')
        path = root.xpath('plugin[name="%s"]/pointOfInterest' % pluginName)

        allPoi = []
        for poi in path:
            allPoi.append(poi[1][1].text)

        return allPoi

    # get all attributes of a poi
    def getPOIInfo(self, pluginName, poiName):
        root = etree.parse('temp/Plugins.xml')
        path = root.xpath('plugin[name="%s"]/pointOfInterest' % pluginName)

        attributes = []
        for poi in path:
            if(poi[1][1].text == poiName):
                allAttributes = poi.findall('.//attribute')
                for attribute in allAttributes:
                    attributes.append(attribute.find('value').text)

        while len(attributes) < 4:
            attributes.append("")

        return attributes

    # get all poi types associated with a plugin
    def getPOITypes(self, pluginName):
        root = etree.parse('temp/Plugins.xml')
        path = root.xpath('plugin[name="%s"]/pointOfInterest/name' % pluginName)

        allTypes = []
        for poi in path:
            allTypes.append(poi.text)

        allTypes = list(dict.fromkeys(allTypes))

        return allTypes

    # get all poi with a certain type
    def getPOIFromType(self, pluginName, type):
        root = etree.parse('temp/Plugins.xml')
        path = root.xpath('plugin[name="%s"]/pointOfInterest' % pluginName)

        filteredPoi = []
        for poi in path:
            if poi[0].text == type:
                filteredPoi.append(poi[1][1].text)

        return filteredPoi

    # get all output associated with a plugin
    def getOutput(self, pluginName):
        root = etree.parse('temp/Plugins.xml')
        path = root.xpath('plugin[name="%s"]/output/name' % pluginName)

        allOutput = []
        for output in path:
            allOutput.append(output.text)

        return allOutput

    def deletePlugin(self, pluginName):
        root = etree.parse('temp/Plugins.xml')
        path = root.xpath('plugin[name="%s"]' % pluginName)

        for plugin in path:
            plugin.getparent().remove(plugin)

        newXML = open("temp/Plugins.xml", "wb")
        str = etree.tostring(root, pretty_print=True, encoding='utf-8')
        newXML.write(str)
        newXML.close()
