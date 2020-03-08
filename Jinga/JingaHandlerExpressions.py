#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader



 poi_dic.append((functionsDictionary))




            # load semantics for jing expressions 
        # print(poi_dic)

        template_dir = '/home/mystic/jupyter_projects/BEAT_UI/view/templates'
        file_loader = FileSystemLoader(template_dir)
        env = Environment(loader=file_loader)
        template = env.get_template('POI.txt')

        # render template using python dictionary cause op or any variable 
        output_expression = template.render(poi_dic=poi_dic)

        # print to console 
        # print(output_expression)

        firstRun = "Jinga_ouput_Network.txt"

        # write mockup script to file in project directory 
        with open(firstRun, "w") as file:
            file.write(output_expression)