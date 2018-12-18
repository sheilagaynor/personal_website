from personal_website import app # init file

from flask import render_template, jsonify, request
import pandas as pd
import numpy as np

##==================================================##
##   HOME PAGE                                      ##
##==================================================##
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

##==================================================##
##   RESEARCH                                       ##
##==================================================##
@app.route('/research')
def research():
    return render_template('research.html')

##==================================================##
##   TEACHING                                       ##
##==================================================##
@app.route('/teaching')
def teaching():
    return render_template('teaching.html')

##==================================================##
##   VITA                                           ##
##==================================================##
@app.route('/vita')
def vita():
    return render_template('vita.html')
