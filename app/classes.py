# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 23:54:48 2020

@author: raihaan
"""

class component:
    def __init__(self, name, parent, project):
        self.name = name
        self.parent = parent
        self.project = project['id']
    
    def push(self, valispace,project):
        valispace.post_data(type='component', data="""{
            "name": \""""+ self.name +"""\",
            "description": "",
            "parent": """+ str(self.parent) +""",
            "project": """+ str(self.project) +""",
            "tags": []
        }""")
        return(valispace.get_component_by_name(unique_name=self.name,project_name=project['name'])['id'])
        
    def get(self):
        None
        
        
class vali:
    def __init__(self):
        None
    
    def push(self,valispace):
        valispace.post_data(type='vali', data="""{
            "parent": """+ self.parent +""",
            "shortname": "mass",
            "description": "",
            "unit": "kg",
            "formula": "5",
            "minimum": null,
            "maximum": null,
            "margin_minus": "0",
            "margin_plus": "0",
            "uses_default_formula": false,
            "reference": "",
            "type": null
        }""")

            
