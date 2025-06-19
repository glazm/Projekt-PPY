from flask import Flask
from flask import render_template


app = Flask(__name__)  # Flask constructor


# A decorator used to tell the application
# which URL is associated function
@app.route('/')
def hello():
    return 'HELLO'


if __name__ == '__main__':
    app.run(debug=True)