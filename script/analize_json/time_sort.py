from datetime import datetime as dt
import csv
import argparse
import operator

parser = argparse.ArgumentParser(description='sorted by timezone for data')
parser.add_argument('-i', '--input', default='./data/dataset.csv', type=str)
parser.add_argument('-o', '--output', default='./data/dataset_sorted.csv', type=str)

args = parser.parse_args()
in_file = args.input
out_file = args.output

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
