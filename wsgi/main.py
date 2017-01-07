from flask import Flask
from flask import request
from flask import jsonify
from tableparser import HTMLTableParser
import requests
import re
from json import dumps

app = Flask(__name__)

class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['error'] = self.message
        return rv
        
def fetchhtml(regno,semester,month,year,result_type):
    payload =  {}
    payload['statuscheck'] = 'failed'
    payload['regno'] = regno
    payload['deg_name'] = 'B.Tech'
    payload['semester'] = semester
    payload['month'] = month
    payload['year'] = year
    payload['result_type'] = result_type
    
    try:
        session = requests.session()
        r = requests.post('http://exam.cusat.ac.in/erp5/cusat/CUSAT-RESULT/Result_Declaration/display_sup_result',data=payload)
        return (r.text)
    except :
        build_response = {"details":"unable to connect"}
        return (build_response)

def fetchjson(html):
        marklist = HTMLTableParser()
        marklist.feed(html)
        #print (marklist.tables)
        #print (marklist.br)
        gpa = re.findall(r"[-+]?\d*\.\d+|\d+",marklist.br[0])
        
        details = {}
        for lists in marklist.tables[:1:]:
            for l in lists:
                i=0
                while i<len(l):
                    details[l[i]] = l[i+1]
                    i+=2
            
        #print (details)
            
        marks = {}
        for lists in marklist.tables[1::]:
            subjects = lists[:1:][0]
            for l in lists[1::]:
                marks[l[0]] = l
        #print (marks)
        if len(marks)==0:
            build_response = {"details":"no marks in server"}
            return (build_response)
            
        final = {}
        final['details'] = details
        final['marklist'] = marks
        try:
            final['gpa'] = gpa[0]
        except IndexError:
            final['gpa'] = 'null'
          
        return (final)

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@app.route("/")
def api():
    return "API documentation"
    
@app.route("/fetch/<regno>",methods=['GET'])
def fetch(regno):
    semester = request.args.get('semester')
    month = request.args.get('month')
    year = request.args.get('year')
    result_type = request.args.get('type')
    if result_type is None or year is None or month is None  or semester is None:
        raise InvalidUsage('check documentation', status_code=410)
    try:
        html = fetchhtml(regno,semester,month,year,result_type)
        json = fetchjson (html)
        return (jsonify(json))        
    except:
        build_response = {"details":"error in processing"}
        return (build_response)

if __name__ == "__main__":
    app.run()

