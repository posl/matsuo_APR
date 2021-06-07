#!/bin/sh
gcc main.c -o test2

function func(){
input=$(<data2/input.txt)
./test2 << EOF
$input
EOF
}

result=`func`
echo $result>./data2/result1.txt
cat ./data2/result1.txt | tr ' ' '\n'>data2/result.txt
rm data2/result1.txt
check=`diff ./data2/output.txt ./data2/result.txt`

if test $check -z
then
    echo "test2 success"
    exit 0
else
    echo 'test2 failed'
    exit 1
fi
