from . import app, db
from .models import Temperature, Log
from flask import request, jsonify, render_template, json
import datetime
import time

@app.before_request
def log_request():
    if(not request.path.startswith("/static") and not request.path == "/favicon.ico"):
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

def allowed_file(filename):
    return '.' in filename and filename.split(".")[-1] == "csv"

#Upload CSV File 
@app.route('/upload', methods = ['POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return error("File not found!")
        file = request.files['file']

        if file and allowed_file(file.filename):
            file.save("temp.csv")
            data = pd.read_csv("temp.csv")

            #Check if all Columns are found
            db_columns = ['temperature', 'duration', 'timestamp']
            diff_set = set(db_columns) - set(data.columns)
            if len(diff_set) != 0:
                return error(f"Columns {diff_set} are missing!")

            if 'id' in data.columns:
                db_columns.append('id')

            #Cleaning
            try:
                data['timestamp'] = (pd.to_datetime(data['timestamp']) - pd.Timestamp("1970-01-01")) / pd.Timedelta('1s')     #Date to Unix timestamp seconds
                data['duration'] = pd.to_timedelta(data['duration']).dt.total_seconds()     #Duration to seconds
            except:
                return error("Wrong format")

            #Upload to Database
            data[db_columns].to_sql('Temperature', db.engine)
            return '1'
    return render_template('index.html')

#Get Data
@app.route('/getData', methods = ['POST'])
def getData():
    if request.method == 'POST':
        fromtime = request.form.get('fromtime', 0)
        totime = request.form.get('totime', 999999999999)
        page = request.form.get('page', 0)

        data = Temperature.query.filter(Temperature.timestamp >= fromtime, Temperature.timestamp <= totime).paginate(page, 50, False)
        data = rows2dict(data)
        return jsonify(data)
    return render_template('index.html')

def rows2dict(data, exclude_cols=[]):
    return [{col.name: getattr(x, col.name) for col in x.__table__.columns if col not in exclude_cols} for x in data]

def ifNone(str):
    return (str==None or str == "" or str.lower() == "nan" or str.lower() == "none" or str.lower() == "null")

def error(msg):
    return jsonify({'error': msg}), 401

def strtobool(str):
    if(str.lower() in ["true", "t", 1, "1", "on"]):
        return True
    return False
    