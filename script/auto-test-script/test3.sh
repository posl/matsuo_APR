#!/bin/sh
gcc $1 -o test3

function func(){
input=$(<data3/input.txt)
./test3 << EOF
$input
EOF
}

result=`func`
echo $result>./data3/result.txt
check=`python check.py -d data3`

if test $check = '0'
then
    echo "T"
    exit 0
else
    echo 'F'
    exit 1
fi
