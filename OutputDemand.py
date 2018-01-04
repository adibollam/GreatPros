import sqlite3
import csv

#############----Open Database Connection----#############
db = sqlite3.connect(dbpath)
db.text_factory = lambda x: str(x, 'latin1')
d = db.cursor()

#############----Select Dates----#############

first_date = d.execute("SELECT MIN(DISTINCT Date) from ParsedData").fetchall()[0][0] #must be a string
last_date = d.execute("SELECT MAX(DISTINCT Date) from ParsedData").fetchall()[0][0] #must be a string
dates = d.execute("SELECT DISTINCT Date from ParsedData where date >= '" + first_date + "' and date <= '" + last_date + "' ORDER BY Date").fetchall()

#############----Select for Total Date Range----#############

total_data = d.execute("SELECT city, COUNT(*)  FROM cities as a, parsedData as b WHERE a.zip = b.zip and city !=  ' ' and date >= '" + first_date + "' and date <= '" + last_date + "' GROUP BY city ORDER BY COUNT(*) DESC")
dashed_first_date = '-'.join(first_date.split('/'))
dashed_last_date = '-'.join(last_date.split('/'))
filename = '/Users/adibollam/GreatPros/Python/DataFiles/Parsed/' + dashed_first_date + '--' + dashed_last_date + 'Demand.csv'
output_file = open(filename, 'w+')
with output_file as f:
    writer = csv.writer(f)
    writer.writerow([first_date + '-' + last_date, 'Demand'])
    writer.writerow(['City', 'Leads'])
    for row in total_data:
        writer.writerow([row[0], row[1]])

#############----Select Individual Dates in Date Range----#############

for each in dates:
    date = each[0]
    dashed_date = '-'.join(date.split('/'))
    date_data = d.execute("SELECT city, COUNT(*)  FROM cities as a, parsedData as b WHERE a.zip = b.zip and city !=  ' ' and date = '" + date + "' GROUP BY city ORDER BY COUNT(*) DESC")
    filename = '/Users/adibollam/GreatPros/Python/DataFiles/Parsed/' + dashed_date + 'Demand.csv'
    output_file = open(filename, 'w+')
    with output_file as f:
        writer = csv.writer(f)
        writer.writerow([date, 'Demand'])
        writer.writerow(['City', 'Leads'])
        for row in date_data:
            writer.writerow([row[0], row[1]])

#############----Close File and Connection to Database----#############

db.close()
output_file.close()
