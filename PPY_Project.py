import json
import os

from Moduł1 import loadData
from Moduł2 import retransform
from Moduł3 import readditional_data
from Moduł4 import my_api
from Moduł5 import load
from Moduł5 import save
from flask import Flask

global daf

if __name__ == '__main__':
    with open("config.json") as config:
        conf = json.load(config)
    app = Flask(__name__)

    if len(os.listdir(f'{conf["drop_folder"]}')) != 0 and len(os.listdir(f'{conf["extentCatalog"]}')) != 0:
        pd = load(conf)
        my_api(app, pd)
        app.run(debug=True)
    else:
        daf = loadData(conf)
        daf = retransform(daf)
        daf = readditional_data(daf,conf)
        my_api(app,daf)
        save(daf,conf)
        app.run(debug=True)

