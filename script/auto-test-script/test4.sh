#!/bin/sh
gcc $1 -o test4

function func(){
input=$(<data4/input.txt)
./test4 << EOF
$input
EOF
}

result=`func`
echo $result>./data4/result.txt
check=`python check.py -d data4`

if test $check = '0'
then
    echo "T"
    exit 0
else
    echo 'F'
    exit 1
fi
