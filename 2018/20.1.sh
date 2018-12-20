#/usr/bin/env bash

#cp 20.txt 20.robocopy.txt

for j in {1..20}; do
    echo -n ${j}
    sed -i "s#\([(|]\)[NEWS]|#\1#g" 20.robocopy.txt
    sed -i "s#|[NEWS]\([|)]\)#\1#g" 20.robocopy.txt
    for i in {1..170}; do
        sed -i "s#\([NEWS]\{$i\}[NEWS]*\)|[NEWS]\{$i\}\([|)]\)#\1\2#g" 20.robocopy.txt
        sed -i "s#\([(|]\)[NEWS]\{$i\}|\([NEWS]\{$i\}[NEWS]*\)#\1\2#g" 20.robocopy.txt
        sed -i "s#(\([NEWS]*\))#\1#g" 20.robocopy.txt
        if [ $((i % 10)) = 0 ]; then
            echo -n .
        fi
    done
    sed -i "s#(|[NEWS|]*)##g" 20.robocopy.txt
    sed -i "s#([NEWS|]*|)##g" 20.robocopy.txt
    sed -i "s#([NEWS|]*||[NEWS|]*)##g" 20.robocopy.txt
    echo
done
