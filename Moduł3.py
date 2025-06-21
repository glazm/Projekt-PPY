import json
import os
from contextlib import nullcontext

import pandas as pd
import requests as r
import urllib.request

#import Moduł4


#import urllib.parse


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

print("Before pickling Modul3")
print(pd.read_pickle(cacheFile))
file = pd.read_pickle(cacheFile)
#    print(title)
for index,row in file.iterrows():
#        print(row["Title"])
#        print(row["Name"])
#        print(row["Surname"])
#        print(row["Publisher"])
    t =str(row["Title"]).replace(' ','%20')
    firstName =str(row["Name"]).replace(' ','%20')
    surname =str(row["Surname"]).replace(' ','%20')
#        authorID =""
#        file['Publisher'] = row['Publisher']
#        t='the+lord+of+the+rings'
    urldata = dict()
    try:
        with urllib.request.urlopen(publisherUrl) as url:
            data = json.load(url)
#               print(data)
            urldata = dict(data)
#               print(urldata)
#           print(urldata['docs'])
        urldata = urldata['docs']
        urldata = list(urldata[0].values())[1]
#       urldata = urldata[]
        print(urldata[0])
#            row['Publisher'] = urldata[0]
#            row['Publisher'] = urldata[0]
#            file['Publisher'] = row['Publisher']
        file.at[index,'Publisher'] = urldata[0]
    except:
#            file['Publisher'] = file['Publisher']
        print("No such data")
#        print()

    try:
        with urllib.request.urlopen(authorIdUrl) as url:
            data = json.load(url)
            urldata = dict(data)
#            print((list((urldata['docs'][0]).values())[0])[0])
        authorID = (list((urldata['docs'][0]).values())[0])[0]
    except:
        print("No such data")
#        print()
    try:
        with urllib.request.urlopen(authorBioUrl) as url:
            data = json.load(url)
            urldata = dict(data)
        print(urldata['bio'])
        file.at[index, 'Author BIO'] = urldata['bio']
#    print(data['docs'])
    except:
        file.at[index, 'Author BIO'] = ''
        print("No such data")
#        print()
#    print()
#    print("Moduł 3")
#    print(file)
#    print()


#    for index,row in file.iterrows():
#        if file.at[index,'Author BIO'] != nullcontext and file.at[index,'Author BIO'] != '':
#            print(file.at[index,'Author BIO'])

#    print(type(file))
file.to_pickle(cacheFile)
print("After pickling Modul3")
print(pd.read_pickle(cacheFile))
print("Pickling read Modul3")

def additional_data(file) -> pd.DataFrame:
#    resp = r.get("https://openlibrary.org/search.json?title=the+lord+of+the+rings&author=J.R.R.%20Tolkien&fields=author_key/").json()
#    print(file.head(10))
#    t=[]
#    firstName=[]
#    surname=[]
#    for col in file.columns:
#        if 'Title' in col:
#            t = file[col]
#        elif 'Name' in col:
#            firstName = file[col]
#        elif 'Surname' in col:
#            surname = file[col]

    print("Before pickling Modul3")
    print(pd.read_pickle(cacheFile))
#    print(title)
    for index,row in file.iterrows():
#        print(row["Title"])
#        print(row["Name"])
#        print(row["Surname"])
#        print(row["Publisher"])
        t =row["Title"].replace(' ','%20')
        firstName =row["Name"].replace(' ','%20')
        surname =row["Surname"].replace(' ','%20')
#        authorID =""
#        file['Publisher'] = row['Publisher']
#        t='the+lord+of+the+rings'
        urldata = dict()
        try:
            with urllib.request.urlopen(publisherUrl) as url:
                data = json.load(url)
#               print(data)
                urldata = dict(data)
#               print(urldata)
#           print(urldata['docs'])
            urldata = urldata['docs']
            urldata = list(urldata[0].values())[1]
#       urldata = urldata[]
            print(urldata[0])
#            row['Publisher'] = urldata[0]
#            row['Publisher'] = urldata[0]
#            file['Publisher'] = row['Publisher']
            file.at[index,'Publisher'] = urldata[0]
        except:
#            file['Publisher'] = file['Publisher']
            print("No such data")
#        print()

        try:
            with urllib.request.urlopen(authorIdUrl) as url:
                data = json.load(url)
                urldata = dict(data)
#            print((list((urldata['docs'][0]).values())[0])[0])
            authorID = (list((urldata['docs'][0]).values())[0])[0]
        except:
            print("No such data")
#        print()
        try:
            with urllib.request.urlopen(authorBioUrl) as url:
                data = json.load(url)
                urldata = dict(data)
            print(urldata['bio'])
            file.at[index, 'Author BIO'] = urldata['bio']
#    print(data['docs'])
        except:
            file.at[index, 'Author BIO'] = ''
            print("No such data")
#        print()
#    print()
#    print("Moduł 3")
#    print(file)
#    print()


#    for index,row in file.iterrows():
#        if file.at[index,'Author BIO'] != nullcontext and file.at[index,'Author BIO'] != '':
#            print(file.at[index,'Author BIO'])

#    print(type(file))
    file.to_pickle(cacheFile)
    print("After pickling Modul3")
    print(pd.read_pickle(cacheFile))
    print("Pickling read Modul3")
#    Moduł4.l(file) #comment if you want to test this modul
    return file
#    print(resp.status_code)
 #   print(resp.content)