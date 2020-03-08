import mongoengine
from model.PluginPOI import PluginPOI

class PluginData(mongoengine.Document):
    path = mongoengine.StringField(required=True)
    predefinedDataSet = mongoengine.StringField(required=True)
    name = mongoengine.StringField(required=True)
    description = mongoengine.StringField()
    pluginPOI = mongoengine.EmbeddedDocumentListField(PluginPOI)

    meta = {
        'db_alias': 'core',
        'collection': 'Plugins'
    }
