import pandas as pd
import os
import time

import Moduł2

while len(os.listdir('file')) == 0:
    print("Nie ma pliku")
    time.sleep(1)

for file in os.listdir('file'):
    print(file.title())
    print()
    if file.endswith('.csv'):
#        Moduł2.trancsv(file)
        f = pd.read_csv(f'file/{file}')
        Moduł2.tran(f)
    elif file.endswith('.xlsx'):
#        Moduł2.tranxlsx(file)
        f = pd.read_excel(f'file/{file}')
        Moduł2.tran(f)
    else:
        os.remove(f'file/{file}')

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
            return fi
        elif file.endswith('.xlsx'):
            fi = pd.read_excel(f'file/{file}')
#            Moduł2.tranxlsx(file)
            return fi
        else:
            os.remove(f'file/{file}')
            return None
    return None


