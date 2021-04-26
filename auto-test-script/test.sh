#!/bin/sh
N=5

for ((i=1;i<=N;i++))
do 
flag=$(bash test$i.sh)
echo $flag
done
