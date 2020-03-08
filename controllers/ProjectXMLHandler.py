from lxml import etree
from lxml.builder import E

class ProjectXMLHandler(object):

    def loadProjects(self):
        root = etree.parse("Projects.xml").getroot()

        projects = []
        for name in root.iter("name"):
            projects.append(name.text)
        return projects

    def getProjectInfo(self, projectName):
        root = etree.parse("Projects.xml")
        path = root.xpath('project[name="%s"]' % projectName)

        attributes = []
        for project in path:
            attributes.append(project.find('description').text)
            attributes.append(project.find('path').text)
            info = project.find('attributes')
            attributes.append(info.find('os').text)
            attributes.append(info.find('binary').text)
            attributes.append(info.find('machine').text)
            attributes.append(info.find('clas').text)
            attributes.append(info.find('bits').text)
            attributes.append(info.find('language').text)
            attributes.append(info.find('canary').text)
            attributes.append(info.find('crypto').text)
            attributes.append(info.find('nx').text)
            attributes.append(info.find('pic').text)
            attributes.append(info.find('relocs').text)
            attributes.append(info.find('stripped').text)

        return attributes

    def saveNewProject(self, attributes):
        allProjects = self.loadProjects()

        for project in allProjects:
            if project in attributes[0]:
                return "A project with the same name already exists"

        project = (
            E.project (
                E.name(attributes[0]),
                E.description(attributes[1]),
                E.path(attributes[2]),
                E.attributes(
                    E.os(attributes[3]),
                    E.binary(attributes[4]),
                    E.machine(attributes[5]),
                    E.clas(attributes[6]),
                    E.bits(attributes[7]),
                    E.language(attributes[8]),
                    E.canary(attributes[9]),
                    E.crypto(attributes[10]),
                    E.nx(attributes[11]),
                    E.pic(attributes[12]),
                    E.relocs(attributes[13]),
                    E.stripped(attributes[14])
                )
            )
        )
        root = etree.parse("Projects.xml", etree.XMLParser(remove_blank_text=True)).getroot()
        root.insert(0, project)

        newXML = open("Projects.xml", "wb")
        str = etree.tostring(root, pretty_print=True)
        newXML.write(str)
        newXML.close()

    def deleteProject(self, projectName):
        root = etree.parse("Projects.xml")
        path = root.xpath('project[name="%s"]' % projectName)

        for project in path:
            project.getparent().remove(project)

        newXML = open("Projects.xml", "wb")
        str = etree.tostring(root, pretty_print=True, encoding='utf-8')
        newXML.write(str)
        newXML.close()





