#! /bin/bash

# Check if the filename is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 filename"
  exit 1
fi

nmap -p 80,443 -iL $1 -oG output-nmap-HTTPServers.txt
nmap -sS -iL $1 -oG output-nmap-SYN.txt
nmap -sU -iL $1 -oG output-nmap-UDP.txt

echo "Nmap completed!"