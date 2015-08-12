#!/usr/bin/env python
from flask import Flask, send_file
app = Flask(__name__)

@app.route('/')
def hello():
    resp = ("<h1>You did it!</h1>"+
           "<img src='/img.gif'/>")
    return resp

@app.route('/img.gif')
def img():
    return send_file('+1.gif', mimetype='image/gif')

if __name__ == "__main__":
    app.run()