#!/usr/bin/env bash

for test in $(/bin/ls *.test*.txt | grep -v result | grep "^${1}"); do
    result=$(python3 ${test/.test*/.py} ${test})
    expected=$(cat ${test/.txt/.result.txt})
    echo -n "${test%.txt}: "
    if [ "${result}" = "${expected}" ]; then
        echo "PASS"
    else
        echo "FAIL [ got ${result}, expected ${expected} ]"
    fi
done
