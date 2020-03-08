import mongoengine
from model.ProjectPOI import ProjectPOI, FunctionD

class Project(mongoengine.Document):
    name = mongoengine.StringField(required=True)
    description = mongoengine.StringField()
    path = mongoengine.StringField(required=True)
    properties = mongoengine.ListField()
    runs = mongoengine.IntField()
    # If embedded in Projects
    projectPOI = mongoengine.EmbeddedDocumentListField(ProjectPOI)
    projectFunctions = mongoengine.EmbeddedDocumentListField(FunctionD)

    meta = {
        'db_alias': 'core',
        'collection': 'projects',
        'strict': False
    }

##Should POIs be stored here to?
