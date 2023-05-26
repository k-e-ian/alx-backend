#!/usr/bin/env python3.8
'''
File: 1-app.py flask app with babel
'''
from flask_babel import Babel
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEAFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@app.route('/', strict_slashes=False)
def index():
    '''
    render the 1-index.html template
    returns: str: rendered HTML content
    '''
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
