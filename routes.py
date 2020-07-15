# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 12:03:44 2020

@author: Raihaan
"""


from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"