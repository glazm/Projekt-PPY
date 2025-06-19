import pandas as pd

import Moduł3


def trancsv(file):
    f = pd.read_csv(f'file/{file}')
#    print(f.head(10))
#    print(f.columns)
    for col in f.columns:
        if 'internal' in col:
            f = f.drop(col, axis=1)
#    print(f.columns)
    f['Name'] = f['Name'].str.capitalize()
    f['Surname'] = f['Surname'].str.capitalize()
#    print(f.head(10))
    f = f[f.eval("Name=='Stephen' & Surname=='King' | Publisher.str.contains('Penguin Random House|Random House',case=False)")]
#    print(f.head(10))
    for col in f.columns:
        f = f.dropna(axis=0,subset=[col], inplace=False)
    print(f.head(10))
    Moduł3.req(f)
def tranxlsx(file):
    f = pd.read_excel(f'file/{file}')
#    print(f.head(10))
#    print(f.columns)
    for col in f.columns:
        if 'internal' in col:
            f = f.drop(col, axis=1)
#    print(f.columns)
    f['Name'] = f['Name'].str.capitalize()
    f['Surname'] = f['Surname'].str.capitalize()
#    print(f.head(10))
    f = f[f.eval("Name=='Stephen' & Surname=='King' | Publisher.str.contains('Penguin Random House|Random House',case=False)")]
#    print(f.head(10))
    for col in f.columns:
        f = f.dropna(axis=0,subset=[col], inplace=False)
    print(f.head(10))
    Moduł3.req(f)
def removeinternal(file):
    for col in file.columns:
        if 'internal' in col:
            file = file.drop(col, axis=1)
    # print(file.columns)