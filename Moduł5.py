import pandas as pd

def serialize(data_frame,conf)-> pd.DataFrame:
    config_json = conf
    data_frame.to_pickle(f'{config_json["extent"]}')
    print("After pickling Modul5")
    print(pd.read_pickle(f'{config_json["extent"]}'))
    print("Pickling read Modul5")
    return pd.read_pickle(f'{config_json["extent"]}')
