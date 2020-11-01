# Cloning a python object - PoC for Streamlit/Flask integration

import valispace

class Runtime(valispace.API):
    def __init__(self, **entries):
        self.__dict__.update(entries)


vs = valispace.API(url='iclrocketry.valispace.com', username = user, password = passwd)
args = vs.__dict__
print(args)
v = Runtime(**args)
print(v)
print(v.__dict__)

project_name = 'Sporadic_Impulse_COTS2020'
project = {'name':project_name, 'id':v.get_project_by_name(name=project_name)[0]['id']}
print(project)