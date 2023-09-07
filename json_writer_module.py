import json

def json_run():
    #files to read from 
    data_read = open('data.txt', 'r')


        #process data and write to json file
    for x in data_read:
        y = x.split(',')
            
        json_data = {"First" : y[1].strip(), "Last" : y[0].strip(), "Email" : y[2].strip(), "Address" : y[3].strip(), "Phone" : y[4].strip() }
            
        with open('data.json', 'a') as f:
            data = json.dumps(json_data, sort_keys=True, indent=4 * ' ')
            f.write(data + '\n')

    data_read.close()
            
