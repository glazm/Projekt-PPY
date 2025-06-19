import json

import pandas as pd
import requests as r
import urllib.request
#import urllib.parse

def req(file):
#    resp = r.get("https://openlibrary.org/search.json?title=the+lord+of+the+rings&author=J.R.R.%20Tolkien&fields=author_key/").json()

    urldata = dict()
    with urllib.request.urlopen("https://openlibrary.org/search.json?title=the+lord+of+the+rings&author=J.R.R.%20Tolkien&fields=title,publisher,author_name") as url:
        data = json.load(url)
#        print(data)
        urldata = dict(data)
#        print(urldata)
#    print(urldata['docs'])
    urldata = urldata['docs']
    urldata = list(urldata[0].values())[1]
#    urldata = urldata[]
    print(urldata[0])

    with urllib.request.urlopen("https://openlibrary.org/search.json?title=the+lord+of+the+rings&author=J.R.R.%20Tolkien&fields=author_key") as url:
        data = json.load(url)
        urldata = dict(data)
    print((list((urldata['docs'][0]).values())[0])[0])
    with urllib.request.urlopen("https://openlibrary.org/authors/OL26320A.json") as url:
        data = json.load(url)
        urldata = dict(data)
    print(urldata['bio'])
#    print(data['docs'])
    print()
    print("Moduł 3")
    print(file)

#    print(resp.status_code)
 #   print(resp.content)