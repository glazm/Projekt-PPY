import pandas as pd
import os
import time

from pandas import DataFrame

import Moduł2

while len(os.listdir('file')) == 0:
    print("Nie ma pliku")
    time.sleep(1)

for file in os.listdir('file'):
    print(file.title())
    print()
    f=DataFrame
    if file.endswith('.csv'):
#        Moduł2.trancsv(file)
        f = pd.read_csv(f'file/{file}')
#        f.to_pickle('workingFiles/file.json')
#        print("After pickling")
#        print(pd.read_pickle('workingFiles/file.json'))
#        print("Pickling read")
#        Moduł2.tran(f)
    elif file.endswith('.xlsx'):
#        Moduł2.tranxlsx(file)
        f = pd.read_excel(f'file/{file}')
#        f.to_pickle('workingFiles/file.json')
#        print("After pickling")
#        print(pd.read_pickle('workingFiles/file.json'))
#        print("Pickling read")
#        Moduł2.tran(f)
    else:
        os.remove(f'file/{file}')
    f.to_pickle('workingFiles/file.json')
    print("After pickling Modul1")
    print(pd.read_pickle('workingFiles/file.json'))
    print("Pickling read Modul1")
    Moduł2.tran(f)

def prep() -> pd.DataFrame:
    while len(os.listdir('file')) == 0:
        print("Nie ma pliku")
        time.sleep(1)

    for file in os.listdir('file'):
        print(file.title())
        print()
        if file.endswith('.csv'):
            fi = pd.read_csv(f'file/{file}')
#            Moduł2.trancsv(file)
            fi.to_pickle('workingFiles/file.json')
            print("After pickling Modul1")
            print(pd.read_pickle('workingFiles/file.json'))
            print("Pickling read Modul1")
            return fi
        elif file.endswith('.xlsx'):
            fi = pd.read_excel(f'file/{file}')
#            Moduł2.tranxlsx(file)
            fi.to_pickle('workingFiles/file.json')
            print("After pickling Modul1")
            print(pd.read_pickle('workingFiles/file.json'))
            print("Pickling read Modul1")
            return fi
        else:
            os.remove(f'file/{file}')
            return None
#        f.to_pickle('workingFiles/file.json')
#        print("After pickling Modul1")
#        print(pd.read_pickle('workingFiles/file.json'))
#        print("Pickling read Modul1")
    return None


