import pandas as pd

def retransform(file) -> pd.DataFrame:
    for col in file.columns:
        if 'internal' in col:
            file = file.drop(col, axis=1)
    file['Name'] = file['Name'].str.capitalize()
    file['Surname'] = file['Surname'].str.capitalize()
    file = file[file.eval("Name=='Stephen' & Surname=='King' | Publisher.str.contains('Penguin Random House|Random House',case=False)")]
    for col in file.columns:
        file = file.dropna(axis=0,subset=[col], inplace=False)
    return file