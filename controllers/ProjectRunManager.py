def name_to_database(project_name, plugin_name, run):
    space = "___"
    return project_name + space + plugin_name + space + str(run)

def databse_to_name(databse_name):
    space = "___"
    return databse_name.split(space)
