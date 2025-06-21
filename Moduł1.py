import json

import pandas as pd
import os
import time

from pandas import DataFrame

#import Moduł2 #comment if you want no duplicates

with open("config.json") as config:
    conf = json.load(config)
    print("Loaded config.json")

dropFolder = os.listdir(f'{conf["drop_folder"]}')
dropFolderPath = f'{conf["drop_folder"]}'
acceptableFormats = conf["acceptable_formats"]
cacheFile = f'{conf["extent"]}'
print(acceptableFormats)

while len(os.listdir(f'{conf["drop_folder"]}')) == 0:
    print("Nie ma pliku")
    time.sleep(1)



print(conf['system_name'])
for file in dropFolder: #os.listdir('file'):
    print(file)
    print()
    f=DataFrame
    if file.endswith('.csv') and file in acceptableFormats:
#        Moduł2.trancsv(file)
        f = pd.read_csv(f'{dropFolderPath}/{file}') #(f'file/{file}')
#        f.to_pickle('workingFiles/file.json')
#        print("After pickling")
#        print(pd.read_pickle('workingFiles/file.json'))
#        print("Pickling read")
#        Moduł2.tran(f)
        f.to_pickle(cacheFile)
        print("After pickling Modul1")
        print(pd.read_pickle(cacheFile))
        print("Pickling read Modul1")
#        Moduł2.transform(f)  # comment if you want to test this modul
    elif file.endswith('.xlsx') and file in acceptableFormats:
#        Moduł2.tranxlsx(file)
        f = pd.read_excel(f'{dropFolderPath}/{file}') #(f'file/{file}')
#        f.to_pickle('workingFiles/file.json')
#        print("After pickling")
#        print(pd.read_pickle('workingFiles/file.json'))
#        print("Pickling read")
#        Moduł2.tran(f)
        f.to_pickle(cacheFile)
        print("After pickling Modul1")
        print(pd.read_pickle(cacheFile))
        print("Pickling read Modul1")
#        Moduł2.transform(f)  # comment if you want to test this modul
    else:
        os.remove(f'{dropFolderPath}/{file}') #(f'file/{file}')
#    f.to_pickle(cacheFile)
#    print("After pickling Modul1")
#    print(pd.read_pickle(cacheFile))
#    print("Pickling read Modul1")

#    Moduł2.tran(f)#comment if you want to test this modul

def loadData() -> pd.DataFrame:
    while len(os.listdir(f'{conf["drop_folder"]}')) == 0:
        print("Nie ma pliku")
        time.sleep(1)

    for file in dropFolder:
        print(file.title())
        print()
        if file.endswith('.csv') and file in acceptableFormats:
            fi = pd.read_csv(f'{dropFolderPath}/{file}')
#            Moduł2.trancsv(file)
            fi.to_pickle(cacheFile)
            print("After pickling Modul1 from Modul4")
            print(pd.read_pickle(cacheFile))
            print("Pickling read Modul1 from Modul4")
            return fi
        elif file.endswith('.xlsx') and file in acceptableFormats:
            fi = pd.read_excel(f'{dropFolderPath}/{file}')
#            Moduł2.tranxlsx(file)
            fi.to_pickle(cacheFile)
            print("After pickling Modul1 from Modul4")
            print(pd.read_pickle(cacheFile))
            print("Pickling read Modul1 from Modul4")
            return fi
        else:
            os.remove(f'{dropFolderPath}/{file}')
            return None
#        f.to_pickle('workingFiles/file.json')
#        print("After pickling Modul1")
#        print(pd.read_pickle('workingFiles/file.json'))
#        print("Pickling read Modul1")
    return None


