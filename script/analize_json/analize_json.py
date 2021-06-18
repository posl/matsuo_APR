import json
import os
import csv
import argparse
from posixpath import join

#時間表示をpythonのtimeのフォーマットに置換する関数
def change_time_string(time):
    time = time.split('.')[0]
    time = time.replace('T',' ')
    return time

decoder = json.JSONDecoder()

parser = argparse.ArgumentParser(description='create data_dir for json analize')
parser.add_argument('-i', '--input', default='./data.jsonl', type=str)

args = parser.parse_args()
in_dir = args.input

try:
    os.mkdir('data')
except FileExistsError:
    print('./data already exists')


#jsonのデコード
#辞書リストに変換
#形式{id:,kind:,time:,window_id:,}
json_data = []
with open( in_dir ) as f:
    line = f.readline()
    while line:
        json_data.append( decoder.raw_decode( line )[ 0 ] )
        line = f.readline()

k=0
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
    except KeyError:
        print("KeyError: " + str(data))
data_list=[['id','time','user_id','user_name_full','code','window_id','commandline','stderr']]
dataset={}#srcとcompを結合
for key in comp:
    if src[key]:
        dataset[key] = src[key]+comp[key]
        data_list.append([key]+dataset[key])

#全データをまとめたcsvfile
with open("./data/dataset.csv",'w',encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(data_list)

user_data_box={}
user_list=[]
#ユーザーのリストを取得
for key in dataset:
    if [dataset[key][1],dataset[key][2]] not in user_list:
        user_list.append([dataset[key][1],dataset[key][2]])
        user_data_box[dataset[key][1]]=[]
print(user_list)#debug

#解析時除外リスト
#[{5822: '松尾 春紀'}, {5833: '松田 雄河'}, {5859: '中村 悠人'}, {5858: '蔵元 宏樹'}, {5860: '杉原 裕太'}]

#ユーザーidとユーザー名の対応表の保存
with open('data/user_list.csv','w',encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['user id','user name'])
    writer.writerows(user_list)

for item in user_list:
    path = os.path.join('data','user_data',str(item[0]))
    try:
        os.makedirs(path)
    except:
        continue

for key in dataset:
    user_id = dataset[key][1]
    user_data_box[user_id].append([key]+dataset[key])

for key in user_data_box:
    path = os.path.join('data','user_data',str(key))
    with open(path + '/' + str(key)+'.csv','w',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id','time','user_id','user_name_full','code','window_id','commandline','stderr'])
        writer.writerows(user_data_box[key])
    for line in user_data_box[key]:
        id = str(line[0])
        codepath=os.path.join(path,id)
        try:
            os.mkdir(codepath)
        except:
            pass
        with open(codepath +'/'+ id + '.c','w',encoding='utf-8') as f1:
            f1.write(line[4])
'''
for i in range(10):
    print(json_data[i])
    print('\n----')
'''
