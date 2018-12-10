# !/home/lee/anaconda3/bin/python3.6
# -*- coding:utf-8 -*-

import json

def JsonFileReader(filepath):
    with open(filepath) as f:
        file = f.read()

    return json.loads(file)
