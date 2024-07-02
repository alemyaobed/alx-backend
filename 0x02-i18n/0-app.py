#!/usr/bin/env python3
''' A flask app to be used for i18n and l10n'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    ''' Renders the index template '''
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True)
