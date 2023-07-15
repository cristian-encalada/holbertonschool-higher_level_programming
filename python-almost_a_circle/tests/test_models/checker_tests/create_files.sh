#!/bin/bash

for ((i=0; i<=82; i++))
do
    filename="main_$i.py"
    touch "$filename"
    echo "Created file: $filename"
done
