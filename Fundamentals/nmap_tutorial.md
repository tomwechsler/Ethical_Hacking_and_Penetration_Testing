# nmap tutorial

## Creating an inventory

root@kali:~# nmap

root@kali:~# nmap | more

root@kali:~# ip a sh

root@kali:~# cat /etc/resolv.conf

root@kali:~# route -n

root@kali:~# nmap -sn 192.168.93.0/24

root@kali:~# nmap -sn 192.168.93.0/24 -v

root@kali:~# nmap -sn 192.168.93.0/24 -oG - | grep Up | awk '{print $2}'
  
root@kali:~# nmap -sn 192.168.93.0/24 -oG - (output in a 'grepable' format)

root@kali:~# nmap -sn 192.168.93.0/24 -oG - | grep Up (the last line in the previous output is no longer displayed)

root@kali:~# nmap -sn 192.168.93.0/24 -oG - | grep Up | awk '{print $2}'

root@kali:~# nmap -sn 192.168.93.0/24 -oG - | grep Up | awk '{print $2}' > targets.txt

root@kali:~# cat targets.txt


## Identification of open ports and services on systems

root@kali:~# cat targets.txt (this is our list from the last scan - let's examine a system)

root@kali:~# nmap 192.168.93.10 (look at the output and point out the closed ports - 1000 most used)

root@kali:~# more /usr/share/nmap/nmap-services (this is 1000 most used - but not sorted great - the third field is the frequency)

> Note: some bash kung-fu and we get a sorting by frequency

root@kali:~# sort -r -k3 /usr/share/nmap/nmap-services | more

Let's run the first scan again.

root@kali:~# nmap 192.168.93.10 (only TCP no UDP - with the standard scan the top 1000 TCP ports are checked no UDP)

root@kali:~# nmap -sU 192.168.93.10 (ATTENTION: UDP scan takes significantly longer)

> Note: We will talk about scan tuning later


## Finding system vulnerabilities

root@kali:~# nmap -sV 192.168.93.10

> Note: Now we already get a list with the open ports and which services are used

Let's have a look at the Exploit-DB website [Exploit Database](https://www.exploit-db.com/) . As you can see, there are several exploits. But we can also use Kali for the search.

root@kali:~# searchsploit -u (update the local database)

root@kali:~# searchsploit dnsmasq

root@kali:~# searchsploit -w dnsmasq (now we get the URL's)

root@kali:~# searchsploit -p 42946 (local path and URL)

root@kali:~# nmap -sV -oX output.xml 192.168.93.10

root@kali:~# searchsploit --nmap output.xml

> Note: We can use searchsploit directly to analyse our xml file for potential vulnerabilities. We will take a closer look at the topic of vulnerability analysis at a later date


## Monitoring Nmap scans with verbose logging

Your client wants you to scan all subnets that are in use. You have received a list. We are expanding the existing list.

root@kali:~# vim subnets.txt

root@kali:~# cat subnets.txt 
192.168.93.0/24
192.168.94.0/24
192.168.147.0/24

Before we start the scans, we check the interfaces - if you have LAN and WLAN - this can already generate a problem.

root@kali:~# nmap --iflist (we want to scan with the correct NIC)

For example:

root@kali:~# nmap -e eth0 192.168.93.200

Back to our job.

root@kali:~# nmap -sV -p1-65535 -iL subnets.txt

Great, the scan is running...or....? Without output how long does the scan take 10s, 10min, 10days?

We interrupt the scan with Ctrl+c

root@kali:~# nmap -sV -p1-65535 -iL subnets.txt -v (-v stands for verbosity - there are 9 levels - but only two should be used -vv or -v2)

Now we know that the scan works.

If you have problems with nmap, you should check your nmap version

root@kali:~# nmap -v

Now check on [NMAP.ORG](https://nmap.org/) if this is the latest version. If you are not sure, then it doesn't hurt to:

root@kali:~# apt-get update && apt-get upgrade -y


## Record scan activities for later reference

Sometimes it is important to record the scan activities in order to be able to provide information later if necessary

Let's start with the following example, which we will discuss in more detail in the nmap section

root@kali:~# nmap -sV 192.168.93.0/24 -v > myscan.txt

Although we use -v we get no output. With the > the output is redirected to the text file

Open a new terminal

root@kali:~# tail -f myscan.txt 

Haaa...the scan is running!


## Finding live hosts in the network

root@kali:~# cat subnets.txt 
192.168.93.0/24
192.168.94.0/24
192.168.147.0/24

root@kali:~# nmap -iL subnets.txt 

Ctrl + c to ^C

root@kali:~# nmap -sL -iL subnets.txt (list the IPs without checking)

root@kali:~# nmap -sL -iL subnets.txt > allhosts.txt

Now we have been authorised to scan all systems. We want to create a list of live hosts

root@kali:~# nmap -sn -iL subnets.txt > livehosts.txt

root@kali:~# cat livehosts.txt

The problem with this list is that it contains too much data. We need a list with one IP per line

root@kali:~# nmap -sn -iL subnets.txt -oG - | grep Up | awk '{print $2}' > livehosts.txt

root@kali:~# cat livehosts.txt 

Much better!!!

Now the customer comes and tells you...oh...I forgot to give you a subnet. Can you scan that too?

Of course!

root@kali:~# nmap -sn 192.168.95.0/24 -oG - | grep Up | awk '{print $2}' >> livehosts.txt

> Note: ATTENTION: Very important the double >> to add the new content!!!

Open new tab

root@kali:~# tail -f livehosts.txt

root@kali:~# cat livehosts.txt

OK, but have we discovered all live hosts? Are all systems in our list?

Let's take another look at a standard scan

root@kali:~# nmap 192.168.93.1-20

But what does this standard scan do?

1. ICMP Echo Request
2. TCP Syn Packet to port 443
3. TCP Ack Packet to port 80
4. ICMP Timestamp

When a host responds to one of these requests, it receives a standard Nmap scan of the thousand most common ports, which we have discussed in a previous step.

root@kali:~# nmap -Pn 192.168.93.1-20

What this does is skip the host discovery part and go straight to port scanning. Now we could customise our previous scan, but this can lead to a very long scan!


## Defining port ranges to make scans more efficient

root@kali:~# nmap -Pn 192.168.93.0/24

This scan starts immediately by checking the ports. There are only a few hosts online in our network. But what if 254 hosts are online? The scan will take a very long time.

root@kali:~# nmap 192.168.93.0/24

This scan scans the 1000 top ports. We remember the following list.

root@kali:~# sort -r -k3 /usr/share/nmap/nmap-services | more

We can also run a scan with the top 100 ports from the nmap list

root@kali:~# nmap -F 192.168.93.0/24

or

root@kali:~# nmap --top-ports 100 192.168.93.0/24

root@kali:~# nmap --top-ports 200 192.168.93.0/24

or we can create our own port list

root@kali:~# nmap -p80,443,53,45000-50000 192.168.93.0/24

Don't forget we only check TCP ports and no UDP ports with these options

root@kali:~# sort -r -k3 /usr/share/nmap/nmap-services | grep udp | more

root@kali:~# nmap -sU 192.168.93.0/24 (again the 1000 top ports)

or

root@kali:~# nmap -sU --top-ports 100 192.168.93.0/24

How about TCP and UDP!!!

root@kali:~# nmap -sTU --top-ports 100 192.168.93.0/24


## Nmap output formats

root@kali:~# nmap 192.168.93.10 > text.txt

root@kali:~# cat text.txt 

The first thing we don't see is when the scan is finished. No problem with one host, but what about 254 hosts?

root@kali:~# nmap 192.168.93.0/24 > when-is-this-scan-finished.txt

> Note: nmap can help us with this!

root@kali:~# nmap -oN text-with-monitoring.txt 192.168.93.0/24 (hit the spacebar that shows the status!)

The disadvantage of pure text files is that they are not easy to search.

root@kali:~# grep 'Host: 192.168.93.10' text-with-monitoring.txt 

No result is returned! The text file is not in a grepable format.

root@kali:~# nmap -oG grepable.txt 192.168.93.0/24

root@kali:~# grep 'Host: 192.168.93.10' grepable.txt 

Ahh, now we get a search result.

root@kali:~# grep 'Status: Up' grepable.txt 

root@kali:~# grep 445/open grepable.txt 

and so on!

root@kali:~# nmap -oX output-in.xml 192.168.93.0/24

The advantage with xml is that we can open this file in Zenmap and import it into Metasploit. To view an xml file in the browser, an HTML format would be very nice.

root@kali:~# xsltproc output-in.xml -o output-in.html

root@kali:~# firefox output-in.html &

Wow, a great view and already the first documentation!

But why not run a scan that creates all common formats, which can then be further analysed later? A good question!

root@kali:~# nmap -oA bigoutput 192.168.93.0/24

root@kali:~# ls -l bigausgabe.*

Three great formats!

root@kali:~# nmap -oA bigoutput 192.168.93.0/24 && xsltproc bigoutput.xml -o bigoutput.html

root@kali:~# ls -l bigausgabe.*

BOOOOM, four formats incl. HTML


## Use of Nmap scripts to automate the network scan

So far we have focused heavily on using Nmap to make an initial discovery of our networks. We have done both extensive and very targeted scans depending on what we are looking for, either to get a good overview of what is in a network, and we have also practised exporting these results into different formats such as XML and HTML. Now that we're getting good at the discovery phase of scanning, the next logical step is to become even more targeted in our investigation of systems. And this is an area where the NSE or Nmap scripting engine really shines. But where are these NSEs on our system?

root@kali:~# locate *.nse

A large selection.

root@kali:~# locate *.nse | wc -l

root@kali:~# cd /usr/share/nmap/scripts/

root@kali:/usr/share/nmap/scripts# ls -l

root@kali:/usr/share/nmap/scripts# ls -l | more

It seems that there are all sorts of interesting scripts here. Some have to do with DNS, FTP, HTTP and more, but the big question is what each of these scripts actually does. Now, one thing we'll pay special attention to is the naming convention of these scripts

root@kali:/usr/share/nmap/scripts# ls *brute*

root@kali:/usr/share/nmap/scripts# ls *vuln*

Now we'll look at how we can find out what each of these scripts can do in a nutshell. However, for these scripts with the word vuln, it is helpful to know that many file names have CVE numbers associated with them. With these CVE numbers we can find out on the Internet what the issue is.

Let's take a closer look at a script

root@kali:/usr/share/nmap/scripts# ls *smb*

root@kali:/usr/share/nmap/scripts# nmap --script-help smb-os-discovery.nse

This tells us that the script is trying to determine the operating system, computer name, domain, workgroup and current time via the SMB protocol. And, we can read a few more comments here about what we might run into with gotchas, as well as an additional help URL

Let's take a look at it right now.

root@kali:~# nmap --script=smb-os-discovery.nse -p445 192.168.93.200

root@kali:~# nmap --script=smb-os-discovery.nse -p445 192.168.93.0/24

root@kali:~# nmap --script=smb-os-discovery.nse -p445 -iL targets.txt

Let's take a look at another script

root@kali:~# nmap --script-help banner.nse

Let's take a look at the help file for another script such as Banner NSE. And, let's open the URL for the associated help file. I want to draw your attention to a couple of things here. One is that this script is categorised under discovery and safe. Remember how we looked at scripts with names containing the words brute or vuln, by navigating around the NSE help section, you can quickly pull up a category like brute and see all the scripts that fall into that category. But what does safe mean, that can be found in the documentation and Categories. Let's take a look at the banner script, but first a 'normal' scan.

root@kali:~# nmap 192.168.93.10

root@kali:~# nmap --script=banner.nse 192.168.93.10

a little more specific

root@kali:~# nmap --script=banner.nse --script-args banner.port=53 192.168.93.10

or only for port 53

root@kali:~# nmap --script=banner.nse -p53 192.168.93.10

root@kali:~# nmap --script=banner.nse -p53 192.168.93.0/24

root@kali:~# nmap --script=banner.nse -p53 192.168.93.0/24 --open


### I hope you enjoyed the tutorial and learned something new!

---
## *HAPPY SCANNING!*
---