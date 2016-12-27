"""The report command."""


from json import dumps

from .base import Base

from .fetch import fetchjson,fetchhtml

import calendar

import pprint

from texttable import Texttable

class Report(Base):
    """Prepare a report of a student"""

    def run(self):
        #print ('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
        
        types_of_results = ["Regular", "Revaluation", "Supplementary","Improvement"]
        years = list(map(str,list(range(int(self.options["<start_year>"]),int(self.options["<end_year>"])+1))))
        
        if self.options['--semester'] == "all":
            semesters = ["1&2","3","4","5","6","7","8"]
        else:
            semesters = [self.options["--semester"]]
        
        marklist = {}
        
        print("This is going to take a lot of time. Please wait.")
        
        for sem in semesters:
            marklist[sem] = {}
            for year in years:
                for result_type in types_of_results:
                    if result_type not in marklist[sem]:
                        marklist[sem][result_type] = {} 
                    for month_num in range(1,13):
                        html = fetchhtml(self.options["<regno>"],sem,calendar.month_name[month_num],year,result_type)
                        response = fetchjson(html)
                        if response != -1:
                            print ("Found "+sem+","+calendar.month_name[month_num]+","+result_type+","+year+": "+response["gpa"])
                            if "total" not in marklist[sem]:
                                marklist[sem]["total"] = []
                            marklist[sem]["total"] = response["gpa"]
                            if "marks" not in marklist[sem][result_type]:
                                marklist[sem][result_type]["marks"] = []
                            marklist[sem][result_type]["marks"].append(response)
                        if self.options['--trimmed'] == False:
                            print ("Checking "+ sem+","+calendar.month_name[month_num]+","+result_type+","+year)
            empty_keys = [k for k,v in marklist[sem].items() if not v]
            for k in empty_keys:
                del marklist[sem][k]
                
        print("Final results:-")
        if self.options["--format"] == "json":
            print(dumps(marklist))
        else:
            print("Python Dictionary:-")
            print (marklist)
                
        add = 0
        count = 0
        rows = []
        for i in marklist:
            if "total" in marklist[i]:
                gpa = marklist[i]["total"]
            else:
                gpa = "null"
                continue
            if gpa == "null":
                gpa = self.options["--custom-gpa"]
            if i == "1&2":
                add+=float(gpa)
                count+=1
            rows.append([i,gpa])
            add+=float(gpa)
            count+=1
        
        rows.sort(key=lambda x: x[0], reverse=False)
        rows.insert(0,["Total",add/count])
        table = Texttable()
        table.add_rows(rows)
        print(table.draw())
