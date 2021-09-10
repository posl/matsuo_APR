#!/bin/sh

gcc $1 -o test5

function func(){
input=$(<data5/input.txt)
./test5 << EOF
$input
EOF
}

result=`func`
echo $result>./data5/result.txt
check=`python check.py -d data5`

if test $check = '0'
then
    echo "T"
    exit 0
else
    echo 'F'
    exit 1
fi
