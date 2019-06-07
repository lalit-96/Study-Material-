#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This is the file that implements a flask server to do inferences. It's the file that you will modify to
# implement the scoring for your own algorithm.

import os
import json
import flask
import pandas as pd
import pickle
import numpy as np
#Define the path
prefix = '/opt/ml/'
model_path = os.path.join(prefix, 'model')
with open(os.path.join(model_path, 'myrf.pkl'), 'rb') as inp:
    model = pickle.load(inp)

app = flask.Flask(__name__)
@app.route('/ping', methods=['GET'])
def ping():
    # Check if the classifier was loaded correctly
    try:
        model
        status = 200
    except:
        status = 400
    return flask.Response(response= json.dumps(' '), status=status, mimetype='application/json' )

@app.route('/invocations', methods=['POST'])
def transformation():
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
    #return result
    return flask.Response(response=result, status=200, mimetype='application/json')

#====================================================
