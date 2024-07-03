#!/usr/bin/env python3
''' A flask app to be used for i18n and l10n'''
from flask import Flask, render_template, request, g
from flask_babel import Babel, _


class Config:
    ''' Configuration class for Babel '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app=app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    ''' Gets a user from the mock user data above '''
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None

@app.before_request
def before_request():
    ''' Executes this functionality before '''
    logged_in_user = get_user()
    if logged_in_user:
        g.user = logged_in_user


@babel.localeselector
def get_locale():
    ''' The locale selector function '''
    request_locale = request.args.get('locale')
    if request_locale and request_locale in app.config['LANGUAGES']:
        return request_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    ''' Renders the index template with babel featured '''
    locale = get_locale()
    return render_template("5-index.html", locale=locale)


if __name__ == "__main__":
    app.run(debug=True)
