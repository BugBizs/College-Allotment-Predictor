import re
import csv
from collections import OrderedDict
f1=open("pdftext.txt",'r')
text=f1.read()
f1.close()

def findBranches():
    BranchCodes=[]
    colleges=re.findall(r'\n[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9] -.*\n', text)
    colleges_1=[]
    for college in colleges:
        colleges_1.append(college.replace("\n",""))
        BranchCodes=[]
        for codes in colleges_1:
            BranchCodes.append(codes[0:9])
            
    return BranchCodes


def findCollegeAndInscode():
    colleges=re.findall(r'\n[0-9][0-9][0-9][0-9] -.*\n', text)
    # Remove \n from each list item
    colleges_1=[]
    for college in colleges:
        colleges_1.append(college.replace("\n",""))
        collegeUnique = list(OrderedDict.fromkeys(colleges_1))
    return collegeUnique



        
with open('college_list.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Institute_code", "College_Name"])
    for rows in b:
        temp=rows.split(" - ")
        writer.writerow(temp)
print("Done...Check the working directory for csv file")



 


    
