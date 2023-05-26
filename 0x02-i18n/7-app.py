#!/usr/bin/env python3.8
'''
File: 7-app.py
'''
from flask_babel import Babel, gettext
from flask import Flask, render_template, request, g
from datetime import datetime
import pytz

app = Flask(__name__, template_folder='templates')
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    '''
    Configuration class for Flask app
    '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_user():
    '''
    Returns user dictionary if ID exists
    '''
    id = request.args.get("login_as")
    if id and int(id) in users:
        return users[int(id)]
    return None


@app.before_request
def before_request():
    '''
    global user func
    '''
    g.user = get_user()


@app.route('/', strict_slashes=False)
def index():
    '''
    render the 6-index.html template
    returns: str: rendered HTML content
    '''
    return render_template('6-index.html',
                           title=gettext('home_title'),
                           header=gettext('home_header'))


@babel.localeselector
def get_locale():
    '''
    determine the best-matcing language from the supported ;ang'''
    local = request.args.get('locale')
    if local and local in app.config["LANGUAGES"]:
        return local
    if get_user():
        local = get_user()["locale"]
        if local and local in app.config["LANGUAGES"]:
            return local
    local = request.headers.get("locale")
    if local and local in app.config["LANGUAGES"]:
        return local
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    '''
    find timezone parameter o/w from usr settings o/w default to utc
    '''
    time_z = request.args.get("timezone")
    try:
        pytz.timezone(time_z)
        return time_z
    except pytz.exceptions.UnknownTimeZoneError:
        pass
    if g.user:
        time_z = g.user["timezone"]
        try:
            pytz.timezone(tz)
            return time_z
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    return pytz.timezone(app.config["BABEL_DEFAULT_TIMEZONE"])



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
