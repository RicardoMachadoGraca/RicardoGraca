#!/bin/bash

# Statement to inform user about the copy
echo "File is copied to the current directory"

# Copies /var/log/syslog to the current working directory

cp /c/Users/Trabalho/Desktop/VSCode-trabalho/Ops-301/log/syslog.txt .

currentdate=$(date)

# Statement to inform user about the time of the copy
echo $currentdate