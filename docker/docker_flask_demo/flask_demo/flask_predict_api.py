#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import json
import flask
import pickle
import pandas as pd
import numpy as np

with open('./myrf.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

app = flask.Flask(__name__)

@app.route('/')
def ping():
    return "Hello world"


@app.route('/predict')
def predict_iris():
    #==========fetch json and convert it into df======
    input_json = flask.request.get_json()
    input_json = json.dumps(input_json['input'])
    input_df = pd.read_json(input_json,orient='list')
    input_df=input_df[['s_length','s_width','p_length','p_width']]
#======make prediction==========================
    prediction = model.predict(input_df.values)
#==========conver result back to json==========
    result = {'output': []}
    list_out = []
    for label in prediction:
        row_format = {'label': int(label)}
        list_out.append(row_format)
    result['output'] = list_out
    result = json.dumps(result)
    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
