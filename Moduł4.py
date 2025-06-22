from flask import request


def my_api(app,file):
    @app.route('/booksByAuthor')
    def booksByAuthor():
        query = str(request.args.get('author'))
        ff = file
        f = []
        for index, row in ff.iterrows():
            if str(row['Surname']).casefold() in query.casefold() and str(row['Name'].casefold()) in query.casefold():
                f.append(str(row['Title']))
        t = ', '.join(f)
        return f'Books written by author {query}: {t}'

    @app.route('/loadedBooks')
    def loadedBooks():
        ff = file
        f = []
        for index, row in ff.iterrows():
            f.append(str(row['Title']))
        t = ', '.join(f)
        return f'Loaded books: {t}'

    @app.route('/wordInTitle')
    def wordInTitle():
        query = str(request.args.get('word'))
        ff = file
        f = []
        for index, row in ff.iterrows():
            if query.casefold() in str(row['Title']).casefold():
                f.append(str(row['Title']))
        t = ', '.join(f)
        return f'Titles containing given word "{query}": {t}'