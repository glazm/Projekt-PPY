import json
from Moduł1 import loadData
from Moduł2 import retransform
from Moduł3 import readditional_data
from Moduł4 import my_api
from Moduł5 import load
from Moduł5 import save
from flask import Flask
import pandas as pd

with open("config.json") as config:
    conf = json.load(config)
    print("Loaded config.json")

#bez sprawdzania czy jest plik
pd = load(conf)

app = Flask(__name__)
#data = loadData(conf)
#transform = retransform(data,conf)
#print(transform)
#additional = readditional_data(transform,conf)
#my_api(app,additional)
#save(data,conf)
#Dodatkowy data frame aby łączyć wyniki i odwoływać się do jednego pliku
#PLus lupa dla wyczekiwania na nowe pliki
if __name__ == '__main__':
    app.run(debug=True)

