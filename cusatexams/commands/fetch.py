"""The fetch command."""


from json import dumps

from .base import Base

import requests

def fetchhtml(regno,semester,month,year,result_type):
    payload =  {}
    payload['statuscheck'] = 'failed'
    payload['regno'] = regno
    payload['deg_name'] = 'B.Tech'
    payload['semester'] = semester
    payload['month'] = month
    payload['year'] = year
    payload['result_type'] = result_type
    
    session = requests.session()
    r = requests.post('http://exam.cusat.ac.in/erp5/cusat/CUSAT-RESULT/Result_Declaration/display_sup_result',data=payload)
    return (r.text)
    

class Fetch(Base):
    """Decode HTML, returns JSON"""

    def run(self):
        print ('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
        html = fetchhtml('12140834','3','November','2015','Revaluation')    #Test params.
        print (html)           
