#!/usr/bin/env python3
''' A flask app to be used for i18n and l10n'''
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    ''' Configuration class for Babel '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app=app)


# Locale selector function
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    ''' Renders the index template with babel featured '''
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True)
