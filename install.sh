#!/usr/bin/env bash
# This Programm Write by Mr.nope
# 100 v1.3.0
if [[ "$(id -u)" -ne 0 ]];
then
  echo "
Please, Run This Programm as Root
"
  exit 1
fi
function main() {
    printf '\033]2;100/Installing\a'
    clear
    echo "Installing..."
    chmod +x 100.py
    sleep 1
    apt install python
    apt install python3
    apt install python3-pip
    pip3 install --upgrade pip
    echo "
Finish...!

Usage: 
     python3 100.py
    "
    exit 1
}
main