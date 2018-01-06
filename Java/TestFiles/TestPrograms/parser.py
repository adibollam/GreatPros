import re
from datetime import datetime


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
    output_row_string = getDate(columns[colnum[0]].strip('"')) + ',' + getjobType(columns[colnum[1]]) + ',' + 'x' + ',' + 'x' + ',' + 'x' + ',' + getZip(columns[colnum[1]]) + '\n'
    return output_row_string


colnum = [0,4]

source_file_name = str(input("Source File Name: "))
destination_file_name = str(input("Destination File Name: "))

source_file = open(source_file_name, 'r')
destination_file = open(destination_file_name, 'w')

counter = False
for line in source_file:
    if counter:
        new_row = getNewRow(line)
        destination_file.write(new_row)
    else:
        destination_file.write('Date' + ',' + 'JobType' + ',' + 'Cost' + ',' + 'Sales' + ',' + 'Source' + ',' + 'Zip' + '\n')
    counter = True
destination_file.close()
