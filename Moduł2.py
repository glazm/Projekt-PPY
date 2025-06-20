import pandas as pd

import Moduł3


def tran(file) -> pd.DataFrame:
#    f=[]
#    if file.endswith('.csv'):
#        f = pd.read_csv(f'file/{file}')
#    elif file.endswith('.xlsx'):
#        f = pd.read_excel(f'file/{file}')
#    f = pd.read_csv(f'file/{file}')
#    print(file.head(10))
#    print(file.columns)
    for col in file.columns:
        if 'internal' in col:
            file = file.drop(col, axis=1)
#    print(f.columns)
    file['Name'] = file['Name'].str.capitalize()
    file['Surname'] = file['Surname'].str.capitalize()
#    print(f.head(10))
    file = file[file.eval("Name=='Stephen' & Surname=='King' | Publisher.str.contains('Penguin Random House|Random House',case=False)")]
#    print(f.head(10))
    for col in file.columns:
        file = file.dropna(axis=0,subset=[col], inplace=False)
    print(file.head(10))
#    Moduł3.req(file)
    print(type(file))
    return file
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
#    Moduł3.req(f)
    return f
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
#    Moduł3.req(f)
    return f
def removeinternal(file):
    for col in file.columns:
        if 'internal' in col:
            file = file.drop(col, axis=1)
    # print(file.columns)