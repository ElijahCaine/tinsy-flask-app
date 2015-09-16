#!/usr/bin/env python
from flask import Flask, send_file
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    now = datetime.now()
    resp = ("<h1>You did it!</h1>"+
           "<img src='/img'/>"+
           "<p>Today's date is: "+now.strftime("%Y-%m-%d, %H:%M:%S"))
    return resp

@app.route('/img')
def img():
    return send_file('z.gif', mimetype='image/gif')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
