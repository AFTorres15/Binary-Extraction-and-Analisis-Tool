import mongoengine

class PluginPOI(mongoengine.EmbeddedDocument):
    type = mongoengine.StringField(required=True)
    name = mongoengine.StringField(required=True)
    size_return = mongoengine.StringField()
    data = mongoengine.DictField()
    run = mongoengine.IntField()
    check = mongoengine.BooleanField()

    def to_dict(self):
        content = dict()
        content['type'] = self.type
        content['name'] = self.name
        content['size_return'] = self.size_return
        content['data'] = self.data
        content['run'] = self.run
        content['check'] = self.check
        return content
    meta = {
        'strict': False
    }
