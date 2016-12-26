"""The fetch command."""


from json import dumps

from .base import Base

from ..tableparser import HTMLTableParser

import re
import requests
from texttable import Texttable
from ascii_graph import Pyasciigraph

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
        return ("Couldn't connect. Check your connection.")

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
            return(-1)
            
        final = {}
        final['details'] = details
        final['marklist'] = marks
        try:
            final['gpa'] = gpa[0]
        except IndexError:
            final['gpa'] = 'null'
          
        return (final)
   
class Fetch(Base):
    """Decode HTML, returns JSON"""

    def run(self):
        #print ('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
        html = fetchhtml(self.options["<regno>"],self.options["<sem>"],self.options["<month>"],self.options["<year>"],self.options["<type>"])
        response = fetchjson(html)
        #print (dumps(response, indent=2, sort_keys=True))
        
        if response == -1:
            print("Details unavailable at exam.cusat.ac.in")
            return -1
        
        rows = []
        l1=[]
        l2=[]
        for i,j in response["details"].items():
            l1.append(i)
            l2.append(j)

        rows.append(l1)
        rows.append(l2)
        table = Texttable()
        table.add_rows(rows)
        print(table.draw())
        
        rows = []
        rows.append(["SUBJECT",150])
        for i,j in response["marklist"].items():
            l = []
            l.append(j[1] + " ("+re.findall(r"(?i)\b[a-zA-Z]\b",j[2])[0] + ")")
            l.append(int(re.findall(r"[-+]?\d*\.\d+|\d+",j[2])[0]))
            rows.append(l)
        rows.sort(key=lambda x: x[1], reverse=True)
        graph = Pyasciigraph()
        for line in graph.graph('GPA: '+response["gpa"], rows):
            print(line)
