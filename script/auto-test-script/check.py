import argparse
import sys

parser = argparse.ArgumentParser(description='check output')
parser.add_argument('-d', '--dir', default='./data1', type=str)

args = parser.parse_args()
dir = args.dir
opath = dir+'/output.txt'
rpath = dir+'/result.txt'

o_file = open(opath,"r",encoding="utf-8")
r_file = open(rpath,"r",encoding="utf-8")

output = o_file.read()
result = r_file.read()

o = output.split('\n')
r = result.split('\n')

i=0
for value in o:
    if value != r[i]:
        print("1")
        sys.exit(1)
    i+=1

print("0")
sys.exit(0)