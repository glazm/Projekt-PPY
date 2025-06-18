import pandas as pd

def trancsv(file):
    f = pd.read_csv(f'file/{file}')
    print(f.head(10))
    print(f.columns)
def tranxlsx(file):
    f = pd.read_excel(f'file/{file}')
    print(f.head(10))
    print(f.columns)
    for col in f.columns:
        if 'internal' in col:
            f = f.drop(col, axis=1)
#    removeinternal(f)
    print(f.columns)
    f['Name'] = f['Name'].str.capitalize()
    f['Surname'] = f['Surname'].str.capitalize()
    print(f.head(10))
    

def removeinternal(file):
    for col in file.columns:
        if 'internal' in col:
            file = file.drop(col, axis=1)
    # print(file.columns)