#!/usr/bin/env bash

for task in $(/bin/ls -- *.py | grep "^${1}" | grep -v debug | grep -v __init__); do
    result=$(python3 "${task}")
    expected=$(cat "${task/.py/.answer.txt}")
    echo -n "${task%.py}: "
    if [ "${result}" = "${expected}" ]; then
        echo "PASS"
    else
        echo "FAIL [ got ${result}, expected ${expected} ]"
    fi
done
