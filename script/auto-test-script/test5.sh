#!/bin/sh
gcc main.c -o test5

function func(){
input=$(<data5/input.txt)
./test5 << EOF
$input
EOF
}

result=`func`
echo $result>./data5/result1.txt
cat ./data5/result1.txt | tr ' ' '\n'>data5/result.txt
rm data5/result1.txt
check=`diff ./data5/output.txt ./data5/result.txt`

if test $check -z
then
    echo "test5 success"
    exit 0
else
    echo 'test5 failed'
    exit 1
fi
