import mongoengine

class ProjectPOI(mongoengine.EmbeddedDocument):
    type = mongoengine.StringField(required=True)
    calls = mongoengine.ListField()
    name = mongoengine.StringField(required=True)
    r2Name = mongoengine.StringField(required=True)
    data = mongoengine.ListField()
    comment = mongoengine.StringField()
    check = mongoengine.BooleanField()

class FunctionD(mongoengine.EmbeddedDocument):
    type = mongoengine.StringField(required=True)
    calls = mongoengine.ListField()
    name = mongoengine.StringField(required=True)
    r2Name = mongoengine.StringField(required=True)
    data = mongoengine.EmbeddedDocumentListField(ProjectPOI)
    comment = mongoengine.StringField()
    check = mongoengine.BooleanField()
    returnV = ProjectPOI()

def transferPOI(poi1, poi2):
    poi1.type = poi2.type
    poi1.calls = poi2.calls
    poi1.name = poi2.name
    poi1.r2Name = poi2.r2Name
    poi1.data = poi2.data
    poi1.comment = poi2.comment
    poi1.check = poi2.check
