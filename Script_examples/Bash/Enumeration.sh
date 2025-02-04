#! /bin/bash

# Get domain from user input
if [ -z "$1" ]; then
  echo "Please provide a domain name!"
  exit 1
fi

theHarvester -d $1 -b yahoo, bing > ./output-theharvester.txt
whois $1 > ./output-whois.txt
nslookup $1 > ./output-nslookup.txt
amass enum -v -active -min-for-recursive 2 -d $1 > ./output-amass.txt

echo "Enumeration Complete!"