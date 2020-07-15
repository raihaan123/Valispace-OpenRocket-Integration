# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 12:02:40 2020

@author: Raihaan
"""

import valispace
from classes import component, vali
from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template("success.html")

@app.route('/sign_in', methods=['GET','POST'])
def login():
    if request.method == "POST":
        
        user = request.form['uname']
        passwd = request.form['psw']
        
        valispaceObj = valispace.API(url='iclrocketry.valispace.com', username = user, password = passwd)
        
        project_name = 'SYSTEMS_TEST'

        project = {'name':project_name, 'id':valispaceObj.get_project_by_name(name=project_name)[0]['id']}
        message = "Currently working on the "+project['name']+" project (ID: "+str(project['id'])+")"
        
        response = test(project)
        
        return render_template("response.html", message = message, response = response)
    
    return render_template("login.html")
    



def test(project):
    
    test = component("Test","null",project['id'])
    test.push(valispaceObj)
    return(valispaceObj.get_component_by_name(unique_name="Test", project_name=project['name']))










if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)