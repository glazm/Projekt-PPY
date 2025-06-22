import json
import os
import pandas as pd
from pandas import DataFrame

#from Moduł1 import loadConfigData
from Moduł1 import loadData
from Moduł2 import retransform
#from Moduł3 import readditional_data
from Moduł4 import my_api
from Moduł5 import serialize
#import Moduł3
from flask import Flask
from flask import request

with open("config.json") as config:
    conf = json.load(config)
    print("Loaded config.json")

app = Flask(__name__)
#config = loadConfigData()
data = loadData(conf)
transform = retransform(data,conf)
print(transform)
#additional = readditional_data(transform)
#my_api(app,additional)
my_api(app,transform)
serialize(transform,conf)

if __name__ == '__main__':
    app.run(debug=True)

