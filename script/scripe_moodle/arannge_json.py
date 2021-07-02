import json
import os
import argparse
import csv
import uuid

decoder = json.JSONDecoder()

try:
    os.mkdir('data')
except FileExistsError:
    print('./data already exists')

parser = argparse.ArgumentParser(description='create data_dir for json analize')
parser.add_argument('-i', '--input', default='./data.json', type=str)

args = parser.parse_args()
indata = args.input

json_data = []
with open( indata ) as f:
    line = f.readline()
    while line:
        json_data.append( decoder.raw_decode( line )[ 0 ] )
        line = f.readline()

data = json_data[0]

for i in range(6):
    try:
        os.mkdir('./data/lect%d'%i)
    except FileExistsError:
        print(('./data/lect%d already exists')%i)
    
    '''
    a = [str(j) for j in data['%d'%i]]
    a = "\n".join(a)
    with open("./data/lect%d/data.txt"%i,"w") as f:
        f.write(a)
    '''

    file = open("./data/lect%d/"%i+"lect%d.csv"%i,"w",encoding="utf-8")
    csvfile = csv.writer(file)
    header = ['name','mail','start','finish','log_id']
    csvfile.writerow(header)
    for line in data['%d'%i]:
        log_id = uuid.uuid4()
        line_list = [line['name'],line['mail'],line['start'],line['finish'],log_id]
        csvfile.writerow(line_list)

        try:
            os.mkdir('./data/lect%d'%i+"/%s"%log_id)
        except FileExistsError:
            print(('./data/lect%d'%i+'/%s already exists')%log_id)
        for k in range(1,4):
            if 'ex%d'%k not in line['log'].keys():
                break
            try:
                os.mkdir('./data/lect%d'%i+"/%s"%log_id)
            except FileExistsError:
                pass
            with open("./data/lect%d"%i+"/%s"%log_id+'/ex%d'%k+"code.csv","w",encoding="utf-8") as f:
                csvfile2 = csv.writer(f)
                header = ['step','time','code']
                csvfile2.writerow(header)
                m=1
                for row in line['log']['ex%d'%k]:
                    time = row[0]['time']
                    code = row[1]['code']
                    csvfile2.writerow([str(m),time,code])
                    m+=1
                m=1

    file.close()