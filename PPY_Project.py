import json
from Moduł1 import loadData
from Moduł2 import retransform
from Moduł3 import readditional_data
from Moduł4 import my_api
from Moduł5 import serialize
from flask import Flask

with open("config.json") as config:
    conf = json.load(config)
    print("Loaded config.json")

app = Flask(__name__)
data = loadData(conf)
transform = retransform(data,conf)
print(transform)
additional = readditional_data(transform,conf)
my_api(app,additional)
serialize(transform,conf)
#Dodatkowy data frame aby łączyć wyniki i odwoływać się do jednego pliku
if __name__ == '__main__':
    app.run(debug=True)

