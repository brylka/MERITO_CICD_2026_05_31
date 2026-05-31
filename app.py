import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

test = os.environ.get('TEST', 'brak zmiennej')
app = Flask(__name__)

@app.route('/')
def hello():
    return f'<h1>Witaj MERITO!</h1><p>Zmienna TEST = {test}</p><p>Autor: Bartosz Bryniarski</p>'


if __name__ == '__main__':
    app.run(debug=True)