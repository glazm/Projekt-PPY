import json
import pandas as pd
import urllib.request

def readditional_data(file,conf) -> pd.DataFrame:
    config = conf
    print("Before pickling Modul3")
    print(pd.read_pickle(f'{config["extent"]}'))
    for index,row in file.iterrows():
        t =str(row["Title"]).replace(' ','%20')
        firstName =str(row["Name"]).replace(' ','%20')
        surname =str(row["Surname"]).replace(' ','%20')
        name = firstName + '%20' + surname
        urldata = dict()
#        print(t)
#        print(firstName)
#        print(surname)
#        print(row["Publisher"])
        try:
            with urllib.request.urlopen(f'{config["getPublisherUrl"]}' % (t,name)) as url:
                data = json.load(url)
                urldata = dict(data)
            urldata = urldata['docs']
            urldata = list(urldata[0].values())[1]
#            print(urldata[0])
            file.at[index,'Publisher'] = urldata[0]
        except:
            print(config['getPublisherUrl'])
            print("No such data")
        try:
            with urllib.request.urlopen(f'{config["getAuthorIdUrl"]}'% (t,name)) as url:
                data = json.load(url)
                urldata = dict(data)
            authorID = (list((urldata['docs'][0]).values())[0])[0]
        except:
            print(f'{config["getAuthorIdUrl"]}')
            print("No such data")
        try:
            with urllib.request.urlopen(f'{config["getAuthorBioUrl"]}'% (authorID) ) as url:
                data = json.load(url)
                urldata = dict(data)
#            print(urldata['bio'])
            file.at[index, 'Author BIO'] = urldata['bio']
        except:
            file.at[index, 'Author BIO'] = ''
            print(f'{config["getAuthorBioUrl"]}')
            print("No such data")
#    serialize(file)#zapisywanie po każdej czynności, komentuje bo zapis będzie tylko na koniec w głównym pliku
    return file
