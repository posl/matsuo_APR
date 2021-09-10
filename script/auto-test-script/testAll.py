import glob
import csv
from os import lseek
import subprocess as sub

files = glob.glob('./program/*')
f = open("testlog.csv","w",encoding="utf-8")
outfile = csv.writer(f)
header=['prog','t1','t2','t3','t4','t5','stderr']
outfile.writerow(header)
#files = [item.strip('.c') for item in files]

for file in files:
    proc = sub.run("bash test.sh %s"%file, shell=True,stdout=sub.PIPE,text=True)
    result = proc.stdout
    file = file.lstrip('./')
    file = file.lstrip('program')
    file = file.lstrip('/')

    file = file.rstrip('.c')
    lis = result.split('\n')
    with open("error.txt","r",encoding="utf-8") as f0:
        error = f0.read()
    lis = [1 if item=='T' else 0 for item in lis]
    del lis[-1]
    l = len(lis)
    if error != "":
        lis = [0]*(l+1)
    outfile.writerow([file]+lis+[error])