# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 21:48:40 2020

@author: Raihaan
"""

from classes import component, vali, textvali


# Testing modules, only for reference

def testComponent(project, valispaceObj):
    
    test = component("Test", "null", project)
    test.push(valispaceObj, project)
    return(valispaceObj.get_component_by_name(unique_name="Test", project_name=project['name']))


def testVali(valispaceObj, parent):
    
    test2 = vali(parent,"testVali", 21)
    test2.push(valispaceObj)
    return(valispaceObj.get_vali_list(parent_id=parent))