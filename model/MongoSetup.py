import mongoengine

# initialize database
def global_init():
    mongoengine.register_connection(alias='core', name='beat_database')