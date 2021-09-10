#!/bin/sh

gcc $1 -o test1

function func(){
input=$(<data1/input.txt)
./test1 << EOF
$input
EOF
}

result=`func`
echo $result>./data1/result.txt
check=`python check.py -d data1`

if test $check = '0'
then
    echo "T"
    exit 0
else
    echo 'F'
    exit 1
fi

    