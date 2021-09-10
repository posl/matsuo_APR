import json
import os
import argparse
import uuid
import sqlite3

decoder = json.JSONDecoder()

try:
    os.mkdir('data')
except FileExistsError:
    print('./data already exists')

parser = argparse.ArgumentParser(description='create data_dir for json analize')
parser.add_argument('-i', '--input', default='./data.json', type=str)

args = parser.parse_args()
indata = args.input

json_data = {}
with open( indata ) as f:
    line = f.readline()
    json_data.update( decoder.raw_decode( line )[ 0 ] )
    print(decoder.raw_decode( line )[ 0 ].keys())
    while line:
        json_data.update( decoder.raw_decode( line )[ 0 ] )
        line = f.readline()

data = json_data

dbname='./data/'+str(indata)+'.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()
query='CREATE TABLE TestData(lectid STRING,time DATETIME,user_mail STRING,user_name_full STRING,code STRING)'
insert_data = []
try:
    cur.execute(query)
    cur.commit()
except:
    print(str(dbname)+' alreay exists.')


for i in range(6):
    
    '''
    a = [str(j) for j in data['%d'%i]]
    a = "\n".join(a)
    with open("./data/lect%d/data.txt"%i,"w") as f:
        f.write(a)
    '''

    code_id = ""
    lect_id = ""
    time = ""
    user_mail= ""
    user_name = ""
    code = ""

    for line in data['%s'%i]:
        print(line['name'])
        code_id = uuid.uuid4()
        user_name = line['name']
        user_mail = line['mail']
        for k in range(1,4):
            if 'ex%d'%k not in line['log'].keys():
                break
            lect_id = 'lect%d'%(i+1)+'-'+'%d'%k 
            for row in line['log']['ex%d'%k]:
                time = row[0]['time']
                time = str(21)+time[2:]
                code = row[1]['code']
                insert_data.append(tuple([lect_id,time,user_mail,user_name,code]))

#print(insert_data)
query = 'INSERT INTO TestData values(?,?,?,?,?)'
cur.executemany(query,insert_data)
conn.commit()
conn.close()