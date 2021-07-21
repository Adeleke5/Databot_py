#Adeleke Adekunle
#
#import the required libraries
import csv
import datetime
import re
import json

# instatiated realtime object to name output files
teta = datetime.datetime.now()

# Open/read an already existing csv file from the local dir 
with open('./input_csv/python hands-on - dataset.csv', 'r') as csv_input:
    csv_reader = csv.DictReader(csv_input)
    # print([x for x in csv_reader])
    
    #created an output csv file with a new role obsolete
    with open('./data_output/output%s.csv'% (teta), 'w') as csv_output:
        fieldnames = ['date', 'sku', 'warehouse_location', 'quantity', 'obsolete']
        csv_writer = csv.DictWriter(csv_output, fieldnames = fieldnames)
        csv_writer.writeheader()
        # Created a json file output
        with open('./data_output/%s.json'% (teta), 'w') as outfile:
            csv_json = {}
            csv_json['row'] = []
            for line in csv_reader:
            # print(line)
                
                dateFormat = re.sub('-', '/',line['date'])
                
                # converted each row time to timespamp
                lineTime = datetime.datetime.strptime(dateFormat, '%Y/%m/%d').timestamp()
                refTime = datetime.datetime.strptime('2021/1/1', '%Y/%m/%d').timestamp()
                
                
                is_obsolete = (lineTime < refTime)
                line["obsolete"] = is_obsolete
                print(line)
                
                csv_json['row'].append(line)
                
                json.dump(csv_json, outfile)
                csv_writer.writerow(line)
