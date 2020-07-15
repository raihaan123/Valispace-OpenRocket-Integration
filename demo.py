# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 23:45:33 2020

@author: raihaan
"""

import xml.etree.ElementTree as ET
import valispace
import keyring
from classes import component


# Connecting to the Valispace API
passwd = keyring.get_password('valispace','raihaan.usman19')
valispace = valispace.API(url='iclrocketry.valispace.com', username='raihaan.usman19', password=passwd)


# Select project
project_name = 'SYSTEMS_TEST'

project = {'name':project_name, 'id':valispace.get_project_by_name(name=project_name)[0]['id']}
print("\nCurrently working on the",project['name'],"project (ID: "+str(project['id'])+")")


# Handling the RKT model
tree = ET.parse('test.rkt')
root = tree.getroot()
for lvl3 in root.findall("./"):
    print(lvl3.tag)


# =============================================================================
# tube = component("Test","null",28)
# tube.push(valispace)
# =============================================================================

