import json
from Moduł1 import loadData
from Moduł2 import retransform
from Moduł3 import readditional_data
from Moduł4 import my_api
from Moduł5 import load
from Moduł5 import save
from flask import Flask
import threading
global daf

if __name__ == '__main__':
    with open("config.json") as config:
        conf = json.load(config)

#bez sprawdzania czy jest plik
    pd = load(conf)

    app = Flask(__name__)
#data = loadData(conf)
    daf = loadData(conf)
#dataT = threading.Thread(loadData, args=conf) #loadData(conf)
    daf = retransform(daf)
#transform = retransform(data)
#print(transform)
    daf = readditional_data(daf,conf)
    my_api(app,daf)
    save(daf,conf)
#Petla dla wyczekiwania na nowe pliki i wielowątkowość
#if __name__ == '__main__':
    app.run(debug=True)

