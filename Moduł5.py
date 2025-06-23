import pandas as pd

def load(conf)-> pd.DataFrame:
    config_json = conf
    return pd.read_pickle(f'{config_json["extent"]}')
def save(data_frame,conf):
    config_json = conf
    data_frame.to_pickle(f'{config_json["extent"]}')

