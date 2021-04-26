#!/bin/sh
gcc main.c -o test3

function func(){
input=$(<data3/input.txt)
./test3 << EOF
$input
EOF
}

result=`func`
echo $result>./data3/result1.txt
cat ./data3/result1.txt | tr ' ' '\n'>data3/result.txt
rm data3/result1.txt
check=`diff ./data3/output.txt ./data3/result.txt`

if test $check -z
then
    echo "test3 success"
    exit 0
else
    echo 'test3 failed'
    exit 1
fi
