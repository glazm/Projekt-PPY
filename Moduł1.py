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
        Moduł2.trancsv(file)
    elif file.endswith('.xlsx'):
        Moduł2.tranxlsx(file)
    else:
        os.remove(f'file/{file}')


