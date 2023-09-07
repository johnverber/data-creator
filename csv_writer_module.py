
import csv

def csv_run():
    #files to read from 
    data_read = open('data.txt', 'r')

    #process data and write to csv file
    with open('data.csv', 'w', newline='') as f:
        thewriter = csv.writer(f)

        thewriter.writerow(['Last', 'First', 'Email', 'Address', 'Phone'])
        for x in data_read:
            y = x.split(',')
            thewriter.writerow([y[0].strip(), y[1].strip(), y[2].strip(), y[3].strip(), y[4].strip()])

        data_read.close()
