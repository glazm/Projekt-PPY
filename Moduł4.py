from flask import Flask
from flask import render_template


import pandas as pd
import Moduł1
import Moduł2
import Moduł3
#from Moduł3 import


ppp=pd.DataFrame
app = Flask(__name__)  # Flask constructor


# A decorator used to tell the application
# which URL is associated function
@app.route('/')
def hello():
    return 'HELLO'

@app.route('/books')
def booksByAuthor():
    query = request.args.get('author')
    print("===============")
    print('Moduł4')
    print("===============")
    ff =Moduł3.req(Moduł2.tran(Moduł1.prep()))
    print(ff)
    print(ff['Name'])
    print(ff['Surname'])
    tab = query.split(' ')
    print(tab)
    f=[]
    for index, row in ff.iterrows():
        if row['Surname'] in tab and row['Name'] in tab :
            print(row['Title'])
            f.append(row['Title'])
    print(f)
    t = ', '.join(f)
#    display(ppp.to_string())
    return f'Author: {t}'
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