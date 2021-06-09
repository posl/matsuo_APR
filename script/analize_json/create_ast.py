import ast
import csv
import os

#言語の壁がある...
f=open("data/dataset.csv","r",encoding="utf-8")
infile = csv.reader(f)
header=next(infile)

for line in infile:
    id = str(line[0])
    user_id = str(line[2])
    path = os.path.join('data','user_data',user_id,id)
    with open(path+'/'+id+'.c',"r",encoding="utf-8") as f1:
        code = f1.read()
    try:
        ast_obj = ast.parse(code)
        with open(path+'/'+id+'.txt') as f2:
            f2.write(ast.dump(ast_obj))
    except:
        print(user_id+':'+id)

f.close()