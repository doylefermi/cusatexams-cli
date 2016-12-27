"""The batch command."""


from json import dumps

from .base import Base

from .fetch import fetchjson,fetchhtml

from texttable import Texttable
import re
from tqdm import tqdm
import pprint


class Batch(Base):
    """Batch process results from to regno"""

    def run(self):
        #print ('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
        
        regno_list = list(map(str,list(range(int(self.options["<start_regno>"]),int(self.options["<end_regno>"])+1))))
        pbar = tqdm(regno_list)
        
        responses = []
        table = Texttable()
        
        for regno in pbar:
            html = fetchhtml(regno,self.options["<sem>"],self.options["<month>"],self.options["<year>"],self.options["<type>"])
            response = fetchjson(html)
            
            if response != -1:
                responses.append(response)
            
            pbar.set_description("Processing %s" % regno)
        
        print("")
        tableheader = ["Reg no","Name"] + list(map(str,list(range(1,len(responses[0]['marklist'])+1)))) + ["GPA"]
        width = [10,30]
        
        for i in responses[0]['marklist']:
            width.append(6)
        width.append(4)
        
        table.header(tableheader)
        table.set_precision(2)
        table.set_cols_width(width)
        
        failures = 0
        processed = 0
        subject_fails = {}
        
        i=0
        for response in responses:
            row = []
            row.append(responses[i]['details']['Registration Number'])
            row.append(responses[i]['details']['Student Name'])
            
            subjects = []

            for subj in responses[i]['marklist']:
                subjects.append(subj)
                if subj not in subject_fails:
                    subject_fails[subj] = 0
            subjects.sort()
            
            for subj in subjects:
                grade = re.findall(r"(?i)\b[a-zA-Z]\b",responses[i]['marklist'][subj][2])[0]
                if grade == "F":
                    subject_fails[subj] += 1
                row.append(responses[i]['marklist'][subj][2])
            
            gpa = responses[i]['gpa']
            if responses[i]['gpa'] == "null":
                gpa = "----"
                failures += 1
            row.append(gpa)

            try:
                table.add_row(row)
                processed+=1
            except:
                print("Not in same category: {}".format(row))
            i+=1
        print("\nResults in range {} {} for Semester {} {} exam, {} {}:-\n".format(self.options["<start_regno>"],self.options["<end_regno>"],self.options["<sem>"],self.options["<type>"],self.options["<month>"],self.options["<year>"]))
        print(table.draw())
        
        print("Students failed: {}".format(failures))
        print("Subjectwise failure:")
        pprint.pprint(subject_fails)
        print("Processed: {}".format(processed))
        
