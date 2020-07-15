# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 12:02:40 2020

@author: Raihaan
"""


from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template("success.html")

@app.route('/sign_in', methods=['GET','POST'])
def login():
    if request.method == "POST":
        
        username = request.form['uname']
        password = request.form['psw']
        
        return render_template("success.html")
    
    return render_template("login.html")
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)