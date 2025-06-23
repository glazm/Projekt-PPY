import os

import pandas as pd

def load(conf)-> pd.DataFrame:
    config_json = conf
    return pd.read_pickle(f'{config_json["extent"]}')
def save(data_frame,conf):
    config_json = conf
    data_frame.to_pickle(f'{config_json["extent"]}')
#    readfile = os.listdir(f'{config_json["drop_folder"]}')
#    with open("demofile.txt", "w") as f:
#        f.write("Woops! I have deleted the content!")

