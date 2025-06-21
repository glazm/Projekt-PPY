import json
import os

from flask import Flask
from flask import render_template


import pandas as pd
#import Moduł1
#import Moduł2
#import Moduł3
#from Moduł3 import

with open("config.json") as config:
    conf = json.load(config)
    print("Loaded config.json")

dropFolder = os.listdir(f'{conf["drop_folder"]}')
dropFolderPath = f'{conf["drop_folder"]}'
acceptableFormats = conf["acceptable_formats"]
cacheFile = f'{conf["extent"]}'
publisherUrl = f'{conf["getPublisherUrl"]}'
authorIdUrl = f'{conf["getAuthorIdUrl"]}'
authorBioUrl = f'{conf["getAuthorBioUrl"]}'


ppp=pd.DataFrame
app = Flask(__name__)  # Flask constructor


# A decorator used to tell the application
# which URL is associated function
@app.route('/')
def hello():
    return 'HELLO'

@app.route('/booksByAuthor')
def booksByAuthor():
    query = str(request.args.get('author'))
    print("===============")
    print('Moduł4')
    print("===============")
#    ff =Moduł3.additional_data(Moduł2.transform(Moduł1.loadData()))
    ff =pd.read_pickle(cacheFile)
    print(ff)
    print(ff['Name'])
    print(ff['Surname'])
#    print(ff['Publisher'])
#    print(ff['Author BIO'])
    #tab = query.split(' ')

   # stri = tab[0]
    #print(tab)
    print(query)
    f=[]
    for index, row in ff.iterrows():
        if str(row['Surname']).casefold() in query.casefold() and str(row['Name'].casefold()) in query.casefold() :
            print(row['Title'])
            f.append(str(row['Title']))
    print(f)
    t = ', '.join(f)
#    display(ppp.to_string())
    return f'Books written by author {query}: {t}'
#    return render_template('simple.html',  tables=[ff.to_html(classes='data')], titles=ff.columns.values)
@app.route('/loadedBooks')
def loadedBooks():
    print("===============")
    print('Moduł4')
    print("===============")
#    ff =Moduł3.additional_data(Moduł2.transform(Moduł1.loadData()))
    ff = pd.read_pickle(cacheFile)
    print(ff)
    print(ff['Name'])
    print(ff['Surname'])
    f=[]
    for index, row in ff.iterrows():
        print(row['Title'])
        f.append(str(row['Title']))
    print(f)
    t = ', '.join(f)
#    display(ppp.to_string())
    return f'Loaded books: {t}'
#    return render_template('simple.html',  tables=[ff.to_html(classes='data')], titles=ff.columns.values)
@app.route('/wordInTitle')
def wordInTitle():
    query =str(request.args.get('word'))
    print("===============")
    print('Moduł4')
    print("===============")
#    ff =Moduł3.additional_data(Moduł2.transform(Moduł1.loadData()))
    ff = pd.read_pickle(cacheFile)
    print(ff)
    print(ff['Name'])
    print(ff['Surname'])
#    stri = query.
    f=[]
    for index, row in ff.iterrows():
        print(str(row['Title'])+"<->"+query)
        if query.casefold() in str(row['Title']).casefold():
            print(row['Title'])
            f.append(str(row['Title']))
    print(f)
    t = ', '.join(f)
#    display(ppp.to_string())
    return f'Titles containing given word "{query}": {t}'
#    return render_template('simple.html',  tables=[ff.to_html(classes='data')], titles=ff.columns.values)

#@app.route('/authorBio')
#def authorBio():
#    query =str(request.args.get('author'))
#    print("===============")
#    print('Moduł4')
#    print("===============")
#    ff =Moduł3.req(Moduł2.tran(Moduł1.prep()))
#    print(ff)
#    print(ff['Name'])
#    print(ff['Surname'])
#    stri = query.
#    f=[]
#    i = int(0)
#    for index, row in ff.iterrows():
#        print(row['Title']+"<->"+query)
#        if i == 0 and row['Surname'].casefold() in query.casefold() and row['Name'].casefold() in query.casefold() :
#            print(row['Title'])
#            f.append(row['Title'])
#            i=i+1
#            return f'Author "{query}" bio: {row["Author BIO"]}'
#    print(f)
#    t = ', '.join(f)
#    display(ppp.to_string())
#    return f'Titles containing given word "{query}": {t}'
#    return render_template('simple.html',  tables=[ff.to_html(classes='data')], titles=ff.columns.values)

@app.route('/user')
def user():
    return render_template('user.html', name='Anna')

from flask import request
@app.route('/search')
def search():
    query = request.args.get('q')
    return f'Szukano: {query}'
if __name__ == '__main__':
    app.run(debug=True)

def l(file):
    ppp = file