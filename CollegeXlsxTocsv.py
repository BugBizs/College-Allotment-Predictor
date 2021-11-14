##This script is used to convert the .xlsx file provided by college to the desired format for modelling,such as percetage and college name only

import xlrd 
import csv

loc = ("source.xlsx") 
  
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 

college_list=[]
college_marks_0=[]
college_marks_1=[]

  

for i in range(4,sheet.nrows): 
    college_list.append(sheet.cell_value(i, 3))

for i in range(4,sheet.nrows):
    college_marks_0.append(sheet.cell_value(i,4))

print(len(college_list))
print(len(college_marks_0))
with open('dest.csv', 'w', newline='') as file:  ## creating csv file
    writer = csv.writer(file)
    writer.writerow(["kcet", "college"])
    for rows,rows1 in zip(college_list,college_marks_0):
        if len(str(rows1))<1:  ## if marks value is empty then dont add that name of college
            pass
        
        else:
            writer.writerow([rows1,rows])
    print("Successfully created csv file")
