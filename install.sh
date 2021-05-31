#!/bin/bash
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

pip3 install -r requirements.txt
cp gtfob /usr/local/bin/
chmod +x /usr/local/bin/gtfob

