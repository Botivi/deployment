#!/usr/bin env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 11:43:45 2020

@author: vivie
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html",title_page='Home')


if __name__ == "__main__":
    app.run(debug=True)
