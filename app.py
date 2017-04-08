#!/usr/bin/env python
from flask import Flask, send_file
from datetime import datetime
from os import environ

app = Flask(__name__)

@app.route('/')
def hello():
    now = datetime.now()

    resp =  "<h1>You did it!</h1>"
    resp += "<img src='/img'/>"
    resp += "<p>Today's date is: {}</p>".format(now.strftime("%Y-%m-%d, %H:%M:%S"))

    resp += "<ul>"
    for e in environ:
        resp += "<li>{}:{}</li>".format(e, environ[e])
    resp += "</ul>"

    return resp

@app.route('/img')
def img():
    return send_file('z.gif', mimetype='image/gif')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
