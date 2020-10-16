from . import app, db
from .models import Temperature, Log
from flask import request, jsonify, render_template, json
import datetime
import time

@app.before_request
def log_request():
    params = None
    if request.method == 'GET':
        params = json.dumps(request.args)
    else:
        params = json.dumps(request.form)

    log = Log(path=request.path,
                ip=request.remote_addr,
                timestamp=int(time.time()),
                params=params)
    db.session.add(log)
    db.session.commit()

#Home
@app.route('/', methods = ['GET'])
def home():
    return render_template('index.html')

def ifNone(str):
    return (str==None or str == "" or str.lower() == "nan" or str.lower() == "none")

def error(msg):
    return jsonify({'error': msg}), 401

def strtobool(str):
    if(str.lower() in ["true", "t", 1, "1", "on"]):
        return True
    return False
    