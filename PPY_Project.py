import json
import os
import pandas as pd
import Moduł1
import Moduł2
import Moduł3
from flask import Flask
from flask import request

with open("config.json") as config:
    conf = json.load(config)
    print("Loaded config.json")

dropFolder = os.listdir(f'{conf["drop_folder"]}')
dropFolderPath = f'{conf["drop_folder"]}'
acceptableFormats = conf["acceptable_formats"]
cacheFile = f'{conf["extent"]}'

Moduł1.prep()
Moduł2.tran(pd.read_pickle(cacheFile))
Moduł3.req(pd.read_pickle(cacheFile))

load = Moduł1.prep()
t = Moduł2.tran(pd.read_pickle(cacheFile))
api = Moduł3.req(pd.read_pickle(cacheFile))

app = Flask(__name__)

@app.route('/')
def hello():
    return 'HELLO'

@app.route('/booksByAuthor')
def booksByAuthor():
    query = str(request.args.get('author'))
    print("===============")
    print('Moduł4')
    print("===============")
    ff =Moduł3.req(Moduł2.tran(Moduł1.prep()))
    print(ff)
    print(ff['Name'])
    print(ff['Surname'])
    print(query)
    f=[]
    for index, row in ff.iterrows():
        if row['Surname'].casefold() in query.casefold() and row['Name'].casefold() in query.casefold() :
            print(row['Title'])
            f.append(row['Title'])
    print(f)
    t = ', '.join(f)
    return f'Books written by author {query}: {t}'

@app.route('/loadedBooks')
def loadedBooks():
    print("===============")
    print('Moduł4')
    print("===============")
    ff =Moduł3.req(Moduł2.tran(Moduł1.prep()))
    print(ff)
    print(ff['Name'])
    print(ff['Surname'])
    f=[]
    for index, row in ff.iterrows():
        print(row['Title'])
        f.append(row['Title'])
    print(f)
    t = ', '.join(f)
    return f'Loaded books: {t}'

@app.route('/wordInTitle')
def wordInTitle():
    query =str(request.args.get('word'))
    print("===============")
    print('Moduł4')
    print("===============")
    ff =Moduł3.req(Moduł2.tran(Moduł1.prep()))
    print(ff)
    print(ff['Name'])
    print(ff['Surname'])
    f=[]
    for index, row in ff.iterrows():
        print(row['Title']+"<->"+query)
        if query.casefold() in row['Title'].casefold():
            print(row['Title'])
            f.append(row['Title'])
    print(f)
    t = ', '.join(f)
    return f'Titles containing given word "{query}": {t}'

@app.route('/search')
def search():
    query = request.args.get('q')
    return f'Szukano: {query}'
if __name__ == '__main__':
    app.run(debug=True)

