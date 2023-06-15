#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 20:06:28 2018

@author: vivekkalyanarangan
"""
from flask import Flask, request
from flasgger import Swagger
import numpy as np
import pandas as pd

app = Flask(__name__)
swagger = Swagger(app)


@app.route('/', methods=['GET'])
def add():
    """Example endpoint returning a prediction of iris
    ---
    parameters:
      - name: a
        in: query
        type: number
        required: true
      - name: b
        in: query
        type: number
        required: true
      - name: c
        in: query
        type: number
        required: true
    """
    a = request.args.get("a")
    b = request.args.get("b")
    c = request.args.get("c")
    return str(int(a) + int(b) + int(c) )

if __name__=='__main__':
    app.run(debug=True)
    
# http://127.0.0.1:5000/?a=4&b=4&c=1