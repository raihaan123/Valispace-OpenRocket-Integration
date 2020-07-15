# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 12:02:40 2020

@author: Raihaan
"""


from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("login.html")

@app.route('/auth', methods=['POST'])
def login():
    username = request.form['uname']
    password = request.form['psw']
    return None

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)