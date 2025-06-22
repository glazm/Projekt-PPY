from flask import request


def my_api(app,file):
    @app.route('/booksByAuthor')
    def booksByAuthor():
        query = str(request.args.get('author'))
#        print("===============")
#        print('Moduł4')
#        print("===============")
        #    ff =Moduł3.additional_data(Moduł2.transform(Moduł1.loadData()))
        ff = file
#        print(ff)
#        print(ff['Name'])
#        print(ff['Surname'])
#        print(query)
        f = []
        for index, row in ff.iterrows():
            if str(row['Surname']).casefold() in query.casefold() and str(row['Name'].casefold()) in query.casefold():
#                print(row['Title'])
                f.append(str(row['Title']))
#        print(f)
        t = ', '.join(f)
        return f'Books written by author {query}: {t}'

    @app.route('/loadedBooks')
    def loadedBooks():
 #       print("===============")
 #       print('Moduł4')
 #       print("===============")
        #    ff =Moduł3.additional_data(Moduł2.transform(Moduł1.loadData()))
        ff = file
#        print(ff)
#        print(ff['Name'])
#        print(ff['Surname'])
        f = []
        for index, row in ff.iterrows():
#            print(row['Title'])
            f.append(str(row['Title']))
#        print(f)
        t = ', '.join(f)
        return f'Loaded books: {t}'

    @app.route('/wordInTitle')
    def wordInTitle():
        query = str(request.args.get('word'))
#        print("===============")
#        print('Moduł4')
#        print("===============")
        #    ff =Moduł3.additional_data(Moduł2.transform(Moduł1.loadData()))
        ff = file
#        print(ff)
#        print(ff['Name'])
#        print(ff['Surname'])
        f = []
        for index, row in ff.iterrows():
#            print(str(row['Title']) + "<->" + query)
            if query.casefold() in str(row['Title']).casefold():
#                print(row['Title'])
                f.append(str(row['Title']))
#        print(f)
        t = ', '.join(f)
        return f'Titles containing given word "{query}": {t}'