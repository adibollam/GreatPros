from os.path import isfile, join
from os import listdir
####----####
from datetime import datetime
import re
####----####
import sqlite3
import csv
####----####
import os

#############----Find Files to Load----#############

mypath = "/Users/adibollam/GreatPros/Python/DataFiles/Raw"
datafiles = [f for f in listdir(mypath) if f.endswith(".csv") and isfile(join(mypath, f))]

#############----Data Parsing Functions----#############

def getDate(datecol):
    return datetime.strptime(datecol, '%m/%d/%Y %I:%M:%S %p').strftime('%m/%d/%Y')


def getZip(address):
    zipcode = re.match('.*(Zip=)', address)

    return str(address[zipcode.span()[1]: zipcode.span()[1] + 5])

def getjobType(address):
    jobType = re.match('.*(jobtype=)', address)
    return str(address[jobType.span()[1]:len(address) - 2])

def getNewRow(line):
    tokenize = re.compile('[,]')
    columns = tokenize.split(line)
    #output_row_string =  + ',' +  + ',' +  + ',' +  + ',' + 'x' + ',' + )
    return (getDate(columns[colnum[0]].strip('"')), getjobType(columns[colnum[1]]), 'x', 'x', 'x', getZip(columns[colnum[1]]))

#############----Load Parsed Data Into Table----#############

colnum = [0,4]
dbpath = "/Users/adibollam/GreatPros/Database/master.db"
db = sqlite3.connect(dbpath)
d = db.cursor()
d.execute("""CREATE TABLE IF NOT EXISTS parsedData (
                            Date DATETIME,
                            JobType VARCHAR(60),
                            Cost VARCHAR(1),
                            Sales VARCHAR(1),
                            Source VARCHAR(1),
                            Zip INT
                        );""")
db.commit()
for f in datafiles:
    source_file = open("{0}/{1}".format(mypath, f), 'r')

    skip_first_row = False
    for line in source_file:
        if skip_first_row:
            new_row = getNewRow(line)
            print(new_row)
            d.execute("INSERT OR IGNORE INTO parsedData VALUES " + str(new_row))
            db.commit()
        skip_first_row = True
    source_file.close()
db.close()

#############----Move Files to Processed----#############

for f in datafiles:
    os.rename(mypath + "/" + f, mypath + "/Processed/" + f)
