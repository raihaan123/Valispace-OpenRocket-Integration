# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 12:02:40 2020

@author: Raihaan
"""

import valispace
from classes import component, vali
from flask import Flask, render_template, request, redirect
import os

# Instantiate a Flask server
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/sign_in', methods=['GET','POST'])
def login():
    if request.method == "POST":
        
        user = request.form['uname']
        passwd = request.form['psw']
        
        valispaceObj = valispace.API(url='iclrocketry.valispace.com', username = user, password = passwd)
        
        project_name = 'SYSTEMS_TEST'

        project = {'name':project_name, 'id':valispaceObj.get_project_by_name(name=project_name)[0]['id']}
        message = "Currently working on the "+project['name']+" project (ID: "+str(project['id'])+")"
        
        response1 = testComponent(project, valispaceObj)
        response2 = testVali(valispaceObj,response1['id'])
        
        return render_template("response.html", message = message, response1 = response1, response2 = response2)
    
    return render_template("login.html")
    



def testComponent(project, valispaceObj):
    
    test = component("Test", "null", project)
    test.push(valispaceObj, project)
    return(valispaceObj.get_component_by_name(unique_name="Test", project_name=project['name']))


def testVali(valispaceObj,parent):
    
    test = vali(parent,"testVali",21)
    test.push(valispaceObj)
    return(valispaceObj.get_vali_list(parent_id=parent))





# Start webserver on PaaS provider
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)