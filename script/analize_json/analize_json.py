from cluster import Cluster
import json
import os
import csv
import argparse
from posixpath import join
import sqlite3
from typing import Awaitable
from cluster import Cluster

#時間表示をpythonのtimeのフォーマットに置換する関数
def change_time_string(time):
    time = time.split('.')[0]
    time = time.replace('T',' ')
    return time

decoder = json.JSONDecoder()

parser = argparse.ArgumentParser(description='create data_dir for json analize')
parser.add_argument('-i', '--input', default='data', type=str)

args = parser.parse_args()
in_dir = args.input

try:
    os.mkdir(in_dir)
except FileExistsError:
    print('./'+str(in_dir)+' already exists')


#jsonのデコード
#辞書リストに変換
#形式{id:,kind:,time:,window_id:,}
json_data = []
with open( in_dir+'.jsonl' ) as f:
    line = f.readline()
    while line:
        json_data.append( decoder.raw_decode( line )[ 0 ] )
        line = f.readline()

k=0
counter = 0
#データの抽出
src = {}
comp = {}
for data in json_data:
    try:
        if data[ "kind" ] == 'save':
            src[ data[ "save" ][ "id" ] ] = [ change_time_string(data[ "time" ]), data[ "session" ][ "user_id" ],data['session']['user_name_full'], data[ "save" ][ "code" ] ,data["window_id"]]

        elif data[ "kind" ] == 'compile':
            comp[ data[ "compile" ][ "save_id" ] ] = [ data[ "compile" ][ "commandline" ], data[ "compile" ][ "stderr" ] ]
            # 必要であればstderrは文字列errorを含まない場合からにするように処理しても良い
        elif data["kind"] == 'heartbeat':
            counter+=1
    except KeyError:
        print("KeyError: " + str(data))

header_list = ['id','time','user_id','user_name_full','code','window_id','commandline','stderr']
data_list=[]
dataset={}#srcとcompを結合
for key in comp:
    try:
        if src[key]:
            dataset[key] = src[key]+comp[key]
            data_list.append([key]+dataset[key])
    except KeyError:
        print("KeyError: " + str(key))

lectCluster = Cluster()
d_l = []
for data in data_list:
    d = data+[lectCluster.cluster(data[4])]
    if d==None:
        print(d)
    else:
        d_l.append(d)
data_list=d_l

#全データをまとめたdatabase
dbname = "./"+str(in_dir)+"/"+str(in_dir)+".db"
conn = sqlite3.connect(dbname)
cur = conn.cursor()
try:
    query = 'CREATE TABLE WevlData(id INTEGER PRIMARY KEY,time DATETIME,user_id INTEGER,user_name_full STRING,code STRING,window_id STRING,commandline STRING,stderr STRING,lect_id STRING)'
    cur.execute(query)
    conn.commit()
except:
    print('In table,WevlData already exists.')
inserts = [tuple(item) for item in data_list]
query = 'INSERT INTO WevlData values(?,?,?,?,?,?,?,?,?)'
cur.executemany(query,inserts)
conn.commit()

data_list = header_list+data_list
user_data_box={}
user_list=[]
#ユーザーのリストを取得
for key in dataset:
    if [dataset[key][1],dataset[key][2]] not in user_list:
        user_list.append([dataset[key][1],dataset[key][2]])
        user_data_box[dataset[key][1]]=[]

#ユーザ情報のtableを追加
query="CREATE TABLE User(user_id INTEGER PRIMARY KEY,user_name_full STRING)"
cur.execute(query)
conn.commit()
user_table = [tuple(item) for item in user_list]
print(user_table)
query='INSERT INTO User values(?,?)'
cur.executemany(query,user_table)
conn.commit()
conn.close()

#解析時除外リスト
#[{5822: '松尾 春紀'}, {5833: '松田 雄河'}, {5859: '中村 悠人'}, {5858: '蔵元 宏樹'}, {5860: '杉原 裕太'}]