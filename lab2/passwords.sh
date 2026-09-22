#!/bin/bash

mkdir -p password_files

sort passwords.txt | while IFS= read -r password
do
    echo "$password"
    echo "$password" > "password_files/$password"
done
