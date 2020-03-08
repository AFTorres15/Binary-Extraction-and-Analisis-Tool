from model.Projects import Project
from model.ProjectPOI import ProjectPOI, FunctionD
from controllers import ProjectRunManager as PRM
# Database handler for Projects,and ProjectPOI
#

def get_runs(project_name: str, plugin_name: str):
    run = 1
    while True:
        project = getProject(PRM.name_to_database(project_name, plugin_name, run))
        if project is None:
            break
        run += 1
    return run

# Saves newly created project
def createProject(name: str, desc: str, path: str, properties: list):
    project = Project()
    project.name = name
    project.description = desc
    project.path = path
    project.properties = properties

    project.save()

# Returns a project document by its name
def getProject(name: str):
    project = Project.objects(name=name).first()
    return project

# Returns a list of names of all projects currently saved
def getAllProjects():
    allProjects = Project.objects

    projectNames = []
    for project in allProjects:
        project_name = PRM.databse_to_name(project.name)[0]
        if project_name in projectNames:
            continue
        projectNames.append(project_name)

    return projectNames

# Updates a project's info by its name
def updateProject(currentName: str, newName: str, desc: str):
    project = getProject(currentName)
    Project.objects(id=project.id).update_one(set__description=desc, set__name=newName)
    test = getProject(currentName)
    project = getProject(newName)

    print(project.path)

    return project.name

# Deletes a project document
def deleteProject(name):
    project_main = getProject(name)
    project_main.delete()
    #delete runs
    allProjects = Project.objects
    for project in allProjects:
        if PRM.databse_to_name(project.name)[0] == name:
            project.delete()

def createProjectPOI(type:str,name:str,r2name:str,data,check:bool):
    projectPOI = None
    if(type == "function"):
        projectPOI = FunctionD()
    else:
        projectPOI = ProjectPOI()
    projectPOI.type = type
    projectPOI.name = name
    projectPOI.r2Name = r2name
    projectPOI.data = data
    projectPOI.check = check
    return projectPOI

#Adds POI to project using project's name
def addPOIToProject(name:str, poi:ProjectPOI):
    project = Project.objects(name=name).first()
    project.projectPOI.append(poi)
    project.save()

#Gets Project POI given it's name
def getProjectPOIByName (name:str):
    projectPOI = Project.objects(name=name).first()
    return projectPOI

#Adds a comment to projectPOIs
def addCommentToProjectPOI (comment:str, name:str):
    projectPOI = getProjectPOIByName(name)
    projectPOI.comment = comment

def getCommentFromPOI (POIName:str):
    projectPOI = getProjectPOIByName(POIName)
    comment=projectPOI.comment
    return comment

def getAllPois(name: str):
    project = getProject(name)
    projectPOIs = []

    for project_poi in project.projectPOI:
        projectPOIs.append(project_poi)
    for project_poi in project.projectFunctions:
        projectPOIs.append(project_poi)

    return projectPOIs

def getAllProjectPOIs():
    projects = Project.objects
    projectPOIs = []

    for project in projects:
        for project_poi in project.projectPOI:
            projectPOIs.append(project_poi)
        for project_poi in project.projectFunctions:
            projectPOIs.append(project_poi)

    return projectPOIs

def getAllProjectPOINames():
    allProjectPOIs = Project.objects
    projectPOINames = []
    for project in allProjectPOIs:
        for project_poi in project.projectPOI:
            projectPOINames.append(project_poi.name)

    return projectPOINames

def getRunByNumber (PName:str,poiName:str,run:int):
    poi=getProjectPOIByName(poiName)
    count=0
    for poi.data in poi:
        if count==run:
            return poi.data
    return poi.data

def getPOI(name:str):
    projectPOINames = []

    allProjectPOIs = Project.objects
    projectPOINames = []
    for project in allProjectPOIs:
        for project_poi in project.projectPOI:
            if project_poi.name == name:
                return project_poi
        for project_poi in project.projectFunctions:
            if project_poi.name == name:
                return project_poi
    return None
