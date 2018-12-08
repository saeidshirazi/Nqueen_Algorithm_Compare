#!/bin/bash
clear
#Bash Colour Codes

cyan="\033[00;36m"
CYAN="\033[01;36m"

echo -e "${CYAN} THis Script For Compare GA & MIN-Conflict Algoritm in Nqueen Solver "

python3 Nqueen.py


echo -e "${CYAN} "Finish N-Queen solver with GA algoritm""

python3 mc.py

echo -e "${CYAN} "Finish N-Queen solver with Min-Conflicts algoritm""



