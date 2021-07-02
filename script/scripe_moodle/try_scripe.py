from moodle_in import MoodleScriper
import time
import json
import csv
from datetime import datetime,date

# date, datetimeの変換関数
def json_serial(obj):
    # 日付型の場合には、文字列に変換します
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    # 上記以外はサポート対象外.
    raise TypeError ("Type %s not serializable" % type(obj))


MS = MoodleScriper()

with open(".login","r") as f:
    config=f.read()
    MS.ID = config.split()[0]
    MS.PASS = config.split()[1]

MS.login()

time.sleep(1)

element_list = MS.catch_ex_list()

time.sleep(1)

enem_num=len(element_list)
#enem_num=1


for i in range(enem_num):
    MS.get_data(i)
    result = MS.data[i]
    
    time.sleep(1)


with open("data.json",'w') as f:
    json.dump(MS.data,f,default=json_serial)


MS.driver.quit()