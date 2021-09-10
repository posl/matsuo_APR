#!/bin/sh

gcc $1 -o test2

function func(){
input=$(<data2/input.txt)
./test2 << EOF
$input
EOF
}

result=`func`
echo $result>./data2/result.txt
check=`python check.py -d data2`

if test $check = '0'
then
    echo "T"
    exit 0
else
    echo 'F'
    exit 1
fi
