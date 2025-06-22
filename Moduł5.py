import json

import pandas as pd
from flask import Flask
from pandas import DataFrame

#from Moduł1 import loadConfigData
from PPY_Project import loadConfigData
#file=pd.read_pickle('workingFiles/file.json')
#print("Pickling read Modul1")
#print(file["Author BIO"][2])
config_json = loadConfigData()

def serialize(data_frame)-> pd.DataFrame:
#    config = Moduł1.loadConfigData()
# add try catch
#    if(data_frame is not None):
    data_frame.to_pickle(f'{config_json["extent"]}')
    print("After pickling Modul5")
    print(pd.read_pickle(f'{config_json["extent"]}'))
    print("Pickling read Modul5")
    return pd.read_pickle(f'{config_json["extent"]}')


#app = Flask(__name__)

#if __name__ == '__main__':
#    app.run(debug=True)

