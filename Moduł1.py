import pandas as pd
import os
import time

def loadData(conf) -> pd.DataFrame:
    config_json = conf
    while len(os.listdir(f'{config_json["drop_folder"]}')) == 0:
        print("Nie ma pliku")
        time.sleep(1)
    df = pd.DataFrame()
    for file in os.listdir(f'{config_json["drop_folder"]}'):
        if file.endswith('.csv') and file in config_json["acceptable_formats"]:
            file_csv = pd.read_csv(f'{config_json["drop_folder"]}/{file}')
            if not df.empty:
                df = df.append(file_csv, ignore_index=True)
            else:
                df = file_csv
        elif file.endswith('.xlsx') and file in config_json["acceptable_formats"]:
            file_xlsx = pd.read_excel(f'{config_json["drop_folder"]}/{file}')
            if not df.empty:
                df = df.append(file_xlsx, ignore_index=True)
            else:
                df = file_xlsx
        else:
            os.remove(f'{config_json["drop_folder"]}/{file}')
    return df
