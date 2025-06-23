import json
import pandas as pd
import urllib.request

def readditional_data(file,conf) -> pd.DataFrame:
    config = conf
    for index,row in file.iterrows():
        t =str(row["Title"]).replace(' ','%20')
        firstName =str(row["Name"]).replace(' ','%20')
        surname =str(row["Surname"]).replace(' ','%20')
        name = firstName + '%20' + surname
        urldata = dict()
        try:
            with urllib.request.urlopen(f'{config["getPublisherUrl"]}' % (t,name)) as url:
                data = json.load(url)
                urldata = dict(data)
            urldata = urldata['docs']
            urldata = list(urldata[0].values())[1]
            file.at[index,'Publisher'] = urldata[0]
        except:
            print("=============Error=============")
            print(f'{config["getPublisherUrl"]}' % (t,name))
            print("No Publisher data")
        try:
            with urllib.request.urlopen(f'{config["getAuthorIdUrl"]}'% (t,name)) as url:
                data = json.load(url)
                urldata = dict(data)
            authorID = (list((urldata['docs'][0]).values())[0])[0]
        except:
            print("=============Error=============")
            print(f'{config["getAuthorIdUrl"]}'% (t,name))
            print("No Author Id data")
        try:
            with urllib.request.urlopen(f'{config["getAuthorBioUrl"]}'% (authorID) ) as url:
                data = json.load(url)
                urldata = dict(data)
            file.at[index, 'Author BIO'] = urldata['bio']
        except:
            print("=============Error=============")
            file.at[index, 'Author BIO'] = ''
            print(f'{config["getAuthorBioUrl"]}'% (authorID))
            print("No Author Bio data")
    return file
