from datetime import datetime as dt
import csv
import argparse
import os

parser = argparse.ArgumentParser(description='sorted by timezone for data')
parser.add_argument('-d','--directory',default='data')
parser.add_argument('-i', '--input', default='dataset.csv', type=str)
parser.add_argument('-o', '--output', default='dataset_sorted.csv', type=str)

args = parser.parse_args()
dir = args.directory

in_file = os.path.join(dir,args.input)
out_file = os.path.join(dir,args.output)
f=open(in_file)
infile = csv.reader(f)
header=next(infile)

out_list=[]
for line in infile:
    line[1] = dt.strptime(line[1],'%Y-%m-%d %H:%M:%S')
    out_list.append(line)

sorted_list = sorted(out_list,key=lambda x:x[1])

with open(out_file,'w',encoding='utf-8') as w:
    writer=csv.writer(w)
    writer.writerow(header)
    writer.writerows(sorted_list)

f.close()
