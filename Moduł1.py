import pandas as pd
import os
import time

def loadData(conf) -> pd.DataFrame:
    config_json = conf
    while len(os.listdir(f'{config_json["drop_folder"]}')) == 0:
        print("Nie ma pliku")
        time.sleep(1)
    df = pd.DataFrame()
#    df = []
    for file in os.listdir(f'{config_json["drop_folder"]}'):
        print(file.title())
        print()

        if file.endswith('.csv') and file in config_json["acceptable_formats"]:
            file_csv = pd.read_csv(f'{config_json["drop_folder"]}/{file}')
            if not df.empty:
                df = df.append(file_csv, ignore_index=True)
                print("AFTER APPEND CSV")
                print(df)
            else:
#            serialize(fi)#zapisywanie po każdej czynności, komentuje bo zapis będzie tylko na koniec w głównym pliku
#            for index,row in fi.iterrows():
#                print(row[index])
#                df.append({ 'id':row[index]}, ignore_index=True)
#            print(df.head())
                df = file_csv
                print("If empty csv")
                print(df)

#            return fi
        elif file.endswith('.xlsx') and file in config_json["acceptable_formats"]:
            print("XLSX")
            file_xlsx = pd.read_excel(f'{config_json["drop_folder"]}/{file}')
            if not df.empty:
                df = df.append(file_xlsx, ignore_index=True)
                print("AFTER APPEND XLSX")
                print(df)
            else:
#            serialize(fi)#zapisywanie po każdej czynności, komentuje bo zapis będzie tylko na koniec w głównym pliku
                df = file_xlsx
                print("If empty xlsx")
                print(df)

#            return fi
        else:
            os.remove(f'{config_json["drop_folder"]}/{file}')
            #return None
#    return None
    print('All append')
    return df


