import csv
import math

length = []
width = []
area = []


with open('CareAreas.csv', newline='') as ca_file:
    ca_reader = csv.reader(ca_file)
    for row in ca_reader:
       
        x1, y1 = float(row[1]), float(row[3])
        x2, y2 = float(row[2]), float(row[4])
        
        length.append(x2 - x1)
        width.append(y2 - y1)

area = [length[i] * width[i] for i in range(len(length))]

print("Areas of Care Areas:", area)

with open('metadata.csv',newline='') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        main_size_field = float(row[0])  
        sub_field_size = float(row[1]) 
    
area_main=math.pow(int(main_size_field),2)
s= math.sqrt(area_main)

output_rows=[]
index=0
with open('CareAreas.csv', newline='') as ca_file:
    ca_reader = csv.reader(ca_file)  
    for row in ca_reader:
        x1, y1 = float(row[1]), float(row[3])
        x2_bottom=x1+s
        y2_bottom=y1+s
        output_rows.append([index,x1, x2_bottom,y1, y2_bottom])
        index+=1

with open('main_field_size.csv', 'w', newline='') as output_file:
    #fieldnames = ['x1', 'x2', 'y1', 'y2']
    writer = csv.writer(output_file)
    writer.writerows(output_rows)

area_sub=math.pow(int(sub_field_size),2)
s=math.sqrt(area_sub)
output_rows=[]
index=0
with open('CareAreas.csv', newline='') as ca_file:
    ca_reader = csv.reader(ca_file)  
    for row in ca_reader:
        x1, y1 = float(row[1]), float(row[3])
        x2_bottom=x1+s
        y2_bottom=y1+s
        output_rows.append([index,x1, x2_bottom,y1, y2_bottom])
        index+=1

with open('sub_field_size.csv', 'w', newline='') as output_file:
    #fieldnames = ['x1', 'x2', 'y1', 'y2']
    writer = csv.writer(output_file)
    writer.writerows(output_rows)
