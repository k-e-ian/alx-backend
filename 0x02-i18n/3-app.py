#!/usr/bin/env python3.8
'''
File: 3-app.py flask app with babel and parametrize
'''
from flask_babel import Babel, gettext
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')


class Config:
    '''
    Configuration class for Flask app
    '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    '''
    determine the best-matcing language from the supported ;ang'''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    '''
    render the 3-index.html template
    returns: str: rendered HTML content
    '''
    return render_template('3-index.html',
                           title=gettext('home_title'),
                           header=gettext('home_header'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
