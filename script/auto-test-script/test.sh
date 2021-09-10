#!/bin/sh
N=5

cp $1 ./main.c
gcc main.c -o test> out.txt 2> error.txt

rm out.txt
rm main.c
rm ./test

for ((i=1;i<=N;i++))
do 
flag=$(bash test$i.sh $1)
echo $flag
done
