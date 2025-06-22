import json

import pandas as pd
import os
import time

from pandas import DataFrame

#from Moduł5 import serialize
#from PPY_Project import config

def loadConfigData()->dict:
    with open("config.json") as config:
        conf = json.load(config)
        print("Loaded config.json")
    return conf

def loadData() -> pd.DataFrame:
    config_json = loadConfigData()
    while len(os.listdir(f'{config_json["drop_folder"]}')) == 0:
        print("Nie ma pliku")
        time.sleep(1)

    for file in os.listdir(f'{config_json["drop_folder"]}'):
        print(file.title())
        print()
        if file.endswith('.csv') and file in config_json["acceptable_formats"]:
            fi = pd.read_csv(f'{config_json["drop_folder"]}/{file}')
#            serialize(fi)#zapisywanie po każdej czynności, komentuje bo zapis będzie tylko na koniec w głównym pliku
            return fi
        elif file.endswith('.xlsx') and file in config_json["acceptable_formats"]:
            fi = pd.read_excel(f'{config_json["drop_folder"]}/{file}')
#            serialize(fi)#zapisywanie po każdej czynności, komentuje bo zapis będzie tylko na koniec w głównym pliku
            return fi
        else:
            os.remove(f'{config_json["drop_folder"]}/{file}')
            return None
    return None


