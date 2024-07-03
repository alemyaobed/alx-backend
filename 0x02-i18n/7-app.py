#!/usr/bin/env python3
''' A flask app to be used for i18n and l10n'''
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz
from pytz.exceptions import UnknownTimeZoneError


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
    else:
        g.user = None


@babel.localeselector
def get_locale():
    ''' The locale selector function '''
    # Check URL parameters for locale
    request_locale = request.args.get('locale')
    if request_locale and request_locale in app.config['LANGUAGES']:
        return request_locale

    # Check user settings for locale
    if g.user:
        user_locale = g.user.get('locale')
        if user_locale and user_locale in app.config['LANGUAGES']:
            return user_locale

    # Fall back to request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    ''' The timezone selector function '''
    # Check URL parameters for timezone
    request_timezone = request.args.get('timezone')
    if request_timezone:
        try:
            pytz.timezone(request_timezone)
            return request_timezone
        except UnknownTimeZoneError:
            pass

    # Check user settings for timezone
    if g.user:
        user_timezone = g.user.get('timezone')
        if user_timezone:
            try:
                pytz.timezone(user_timezone)
                return user_timezone
            except UnknownTimeZoneError:
                pass

    # Default to UTC
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route("/")
def index():
    ''' Renders the index template with babel featured '''
    locale = get_locale()
    return render_template("7-index.html", locale=locale)


if __name__ == "__main__":
    app.run(debug=True)
