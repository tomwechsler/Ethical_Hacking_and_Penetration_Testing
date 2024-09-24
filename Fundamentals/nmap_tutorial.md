# NMAP Cheat Sheet

Base nmap Syntax:

```
nmap [ScanType] [Options] {targets}
```
If no port range is specified, Nmap scans the 1,000 most popular ports.

- `-p <port1>-<port2>`: Scans a port range
- `-p <port1>,<port2>,...`: Scans a port list
- `-pU:53,U:110,T20-445`: Mix TCP and UDP
- `-r`: Scans linearly (does not randomize ports)
- `--top-ports <n>`: Scan n most popular ports
- `-p-65535`: Leaving off the initial port in range makes Nmap scan start at port 1
- `-p-`: Leaving off the end port in range makes Nmap scan all ports
- `-F`: (Fast (limited port) scan)

## Port Status

- Open: This indicates that an application is listening for connections on this port.
- Closed: This indicates that the probes were received but there is no application listening on this port.
- Filtered: This indicates that the probes were not received and the state could not be established. It also indicates that the probes are being dropped by some kind of filtering.
- Unfiltered: This indicates that the probes were received but a state could not be established.
- Open/Filtered: This indicates that the port was filtered or open but Nmap couldn’t establish the state.
- Closed/Filtered: This indicates that the port was filtered or closed but Nmap couldn’t establish the state.

## Scan Types

- `-sn`: Probe only (host discovery, not port scan)
- `-sS`: SYN Scan
- `-sT`: TCP Connect Scan
- `-sU`: UDP Scan
- `-sV`: Version Scan
- `-O`: Used for OS Detection/fingerprinting
- `--scanflags`: Sets custom list of TCP using `URG ACK PSH RST SYN FIN` in any order

## Probing Options

- `-Pn`: Don't probe (assume all hosts are up)
- `-PB`: Default probe (TCP 80, 445 & ICMP)
- `-PS<portlist>` : Checks if ssytems are online by probing TCP ports
- `-PE`: Using ICMP Echo Request
- `-PP`: Using ICMP Timestamp Request
- `-PM`: Using ICMP Netmask Request

## Timing Options

- `-T0` (Paranoid): Very slow, used for IDS evasion
- `-T1` (Sneaky): Quite slow, used for IDS evasion
- `-T2` (Polite): Slows down to consume less bandwidth, runs ~10 times slower than default
- `-T3` (Normal): Default, a dynamic timing model based on target responsiveness
- `-T4` (Aggressive): Assumes a fast and reliable network and may overwhelm targets
- `-T5` (Insane): Very aggressive; will likely overwhelm targets or miss open ports

## Nmap Scripting Engine

The full list of Nmap Scripting Engine scripts: http://nmap.org/nsedoc/

`nmap -sC` runs default scripts...

Running individual or groups of scripts:
`nmap --script=<ScriptName>| <ScriptCategory>|<ScriptDir>`
  
Using the list of script arguments:
`nmap --script-args=<Name1=Value1,...>`

Updating the script database:
`nmap --script-updatedb`

# NMAP Tutorial

## Creating an inventory

kali@kali:~# sudo nmap

kali@kali:~# sudo nmap | more

kali@kali:~# ip a sh

kali@kali:~# cat /etc/resolv.conf

kali@kali:~# route -n

kali@kali:~# sudo nmap -sn 192.168.93.0/24

kali@kali:~# sudo nmap -sn 192.168.93.0/24 -v

kali@kali:~# sudo nmap -sn 192.168.93.0/24 -oG - | grep Up | awk '{print $2}'
  
kali@kali:~# sudo nmap -sn 192.168.93.0/24 -oG - (output in a 'grepable' format)

kali@kali:~# sudo nmap -sn 192.168.93.0/24 -oG - | grep Up (the last line in the previous output is no longer displayed)

kali@kali:~# sudo nmap -sn 192.168.93.0/24 -oG - | grep Up | awk '{print $2}'

kali@kali:~# sudo nmap -sn 192.168.93.0/24 -oG - | grep Up | awk '{print $2}' > targets.txt

kali@kali:~# cat targets.txt


## Identification of open ports and services on systems

kali@kali:~# cat targets.txt (this is our list from the last scan - let's examine a system)

kali@kali:~# sudo nmap 192.168.93.10 (look at the output and point out the closed ports - 1000 most used)

kali@kali:~# more /usr/share/nmap/nmap-services (this is 1000 most used - but not sorted great - the third field is the frequency)

> Note: some bash kung-fu and we get a sorting by frequency

kali@kali:~# sort -r -k3 /usr/share/nmap/nmap-services | more

Let's run the first scan again.

kali@kali:~# sudo nmap 192.168.93.10 (only TCP no UDP - with the standard scan the top 1000 TCP ports are checked no UDP)

kali@kali:~# sudo nmap -sU 192.168.93.10 (ATTENTION: UDP scan takes significantly longer)

> Note: We will talk about scan tuning later


## Finding system vulnerabilities

kali@kali:~# sudo nmap -sV 192.168.93.10

> Note: Now we already get a list with the open ports and which services are used

Let's have a look at the Exploit-DB website [Exploit Database](https://www.exploit-db.com/) . As you can see, there are several exploits. But we can also use Kali for the search.

kali@kali:~# searchsploit -u (update the local database)

kali@kali:~# searchsploit dnsmasq

kali@kali:~# searchsploit -w dnsmasq (now we get the URL's)

kali@kali:~# searchsploit -p 42946 (local path and URL)

kali@kali:~# sudo nmap -sV -oX output.xml 192.168.93.10

kali@kali:~# searchsploit --nmap output.xml

> Note: We can use searchsploit directly to analyse our xml file for potential vulnerabilities. We will take a closer look at the topic of vulnerability analysis at a later date


## Monitoring Nmap scans with verbose logging

Your client wants you to scan all subnets that are in use. You have received a list. We are expanding the existing list.

kali@kali:~# vim subnets.txt

kali@kali:~# cat subnets.txt 
192.168.93.0/24
192.168.94.0/24
192.168.147.0/24

Before we start the scans, we check the interfaces - if you have LAN and WLAN - this can already generate a problem.

kali@kali:~# sudo nmap --iflist (we want to scan with the correct NIC)

For example:

kali@kali:~# sudo nmap -e eth0 192.168.93.200

Back to our job.

kali@kali:~# sudo nmap -sV -p1-65535 -iL subnets.txt

Great, the scan is running...or....? Without output how long does the scan take 10s, 10min, 10days?

We interrupt the scan with Ctrl+c

kali@kali:~# sudo nmap -sV -p1-65535 -iL subnets.txt -v (-v stands for verbosity - there are 9 levels - but only two should be used -vv or -v2)

Now we know that the scan works.

If you have problems with nmap, you should check your nmap version

kali@kali:~# sudo nmap -v

Now check on [NMAP.ORG](https://nmap.org/) if this is the latest version. If you are not sure, then it doesn't hurt to:

kali@kali:~# apt-get update && apt-get upgrade -y


## Record scan activities for later reference

Sometimes it is important to record the scan activities in order to be able to provide information later if necessary

Let's start with the following example, which we will discuss in more detail in the nmap section

kali@kali:~# sudo nmap -sV 192.168.93.0/24 -v > myscan.txt

Although we use -v we get no output. With the > the output is redirected to the text file

Open a new terminal

kali@kali:~# tail -f myscan.txt 

Haaa...the scan is running!


## Finding live hosts in the network

kali@kali:~# cat subnets.txt 
192.168.93.0/24
192.168.94.0/24
192.168.147.0/24

kali@kali:~# sudo nmap -iL subnets.txt 

Ctrl + c to ^C

kali@kali:~# sudo nmap -sL -iL subnets.txt (list the IPs without checking)

kali@kali:~# sudo nmap -sL -iL subnets.txt > allhosts.txt

Now we have been authorised to scan all systems. We want to create a list of live hosts

kali@kali:~# sudo nmap -sn -iL subnets.txt > livehosts.txt

kali@kali:~# cat livehosts.txt

The problem with this list is that it contains too much data. We need a list with one IP per line

kali@kali:~# sudo nmap -sn -iL subnets.txt -oG - | grep Up | awk '{print $2}' > livehosts.txt

kali@kali:~# cat livehosts.txt 

Much better!!!

Now the customer comes and tells you...oh...I forgot to give you a subnet. Can you scan that too?

Of course!

kali@kali:~# sudo nmap -sn 192.168.95.0/24 -oG - | grep Up | awk '{print $2}' >> livehosts.txt

> Note: ATTENTION: Very important the double >> to add the new content!!!

Open new tab

kali@kali:~# tail -f livehosts.txt

kali@kali:~# cat livehosts.txt

OK, but have we discovered all live hosts? Are all systems in our list?

Let's take another look at a standard scan

kali@kali:~# sudo nmap 192.168.93.1-20

But what does this standard scan do?

1. ICMP Echo Request
2. TCP Syn Packet to port 443
3. TCP Ack Packet to port 80
4. ICMP Timestamp

When a host responds to one of these requests, it receives a standard Nmap scan of the thousand most common ports, which we have discussed in a previous step.

kali@kali:~# sudo nmap -Pn 192.168.93.1-20

What this does is skip the host discovery part and go straight to port scanning. Now we could customise our previous scan, but this can lead to a very long scan!


## Defining port ranges to make scans more efficient

kali@kali:~# sudo nmap -Pn 192.168.93.0/24

This scan starts immediately by checking the ports. There are only a few hosts online in our network. But what if 254 hosts are online? The scan will take a very long time.

kali@kali:~# sudo nmap 192.168.93.0/24

This scan scans the 1000 top ports. We remember the following list.

kali@kali:~# sort -r -k3 /usr/share/nmap/nmap-services | more

We can also run a scan with the top 100 ports from the nmap list

kali@kali:~# sudo nmap -F 192.168.93.0/24

or

kali@kali:~# sudo nmap --top-ports 100 192.168.93.0/24

kali@kali:~# sudo nmap --top-ports 200 192.168.93.0/24

or we can create our own port list

kali@kali:~# sudo nmap -p80,443,53,45000-50000 192.168.93.0/24

Don't forget we only check TCP ports and no UDP ports with these options

kali@kali:~# sort -r -k3 /usr/share/nmap/nmap-services | grep udp | more

kali@kali:~# sudo nmap -sU 192.168.93.0/24 (again the 1000 top ports)

or

kali@kali:~# sudo nmap -sU --top-ports 100 192.168.93.0/24

How about TCP and UDP!!!

kali@kali:~# sudo nmap -sTU --top-ports 100 192.168.93.0/24


## Nmap output formats

kali@kali:~# sudo nmap 192.168.93.10 > text.txt

kali@kali:~# cat text.txt 

The first thing we don't see is when the scan is finished. No problem with one host, but what about 254 hosts?

kali@kali:~# sudo nmap 192.168.93.0/24 > when-is-this-scan-finished.txt

> Note: nmap can help us with this!

kali@kali:~# sudo nmap -oN text-with-monitoring.txt 192.168.93.0/24 (hit the spacebar that shows the status!)

The disadvantage of pure text files is that they are not easy to search.

kali@kali:~# grep 'Host: 192.168.93.10' text-with-monitoring.txt 

No result is returned! The text file is not in a grepable format.

kali@kali:~# sudo nmap -oG grepable.txt 192.168.93.0/24

kali@kali:~# grep 'Host: 192.168.93.10' grepable.txt 

Ahh, now we get a search result.

kali@kali:~# grep 'Status: Up' grepable.txt 

kali@kali:~# grep 445/open grepable.txt 

and so on!

kali@kali:~# sudo nmap -oX output-in.xml 192.168.93.0/24

The advantage with xml is that we can open this file in Zenmap and import it into Metasploit. To view an xml file in the browser, an HTML format would be very nice.

kali@kali:~# xsltproc output-in.xml -o output-in.html

kali@kali:~# firefox output-in.html &

Wow, a great view and already the first documentation!

But why not run a scan that creates all common formats, which can then be further analysed later? A good question!

kali@kali:~# sudo nmap -oA bigoutput 192.168.93.0/24

kali@kali:~# ls -l bigausgabe.*

Three great formats!

kali@kali:~# sudo nmap -oA bigoutput 192.168.93.0/24 && xsltproc bigoutput.xml -o bigoutput.html

kali@kali:~# ls -l bigausgabe.*

BOOOOM, four formats incl. HTML


## Use of Nmap scripts to automate the network scan

So far we have focused heavily on using Nmap to make an initial discovery of our networks. We have done both extensive and very targeted scans depending on what we are looking for, either to get a good overview of what is in a network, and we have also practised exporting these results into different formats such as XML and HTML. Now that we're getting good at the discovery phase of scanning, the next logical step is to become even more targeted in our investigation of systems. And this is an area where the NSE or Nmap scripting engine really shines. But where are these NSEs on our system?

kali@kali:~# locate *.nse

A large selection.

kali@kali:~# locate *.nse | wc -l

kali@kali:~# cd /usr/share/nmap/scripts/

kali@kali:/usr/share/nmap/scripts# ls -l

kali@kali:/usr/share/nmap/scripts# ls -l | more

It seems that there are all sorts of interesting scripts here. Some have to do with DNS, FTP, HTTP and more, but the big question is what each of these scripts actually does. Now, one thing we'll pay special attention to is the naming convention of these scripts

kali@kali:/usr/share/nmap/scripts# ls *brute*

kali@kali:/usr/share/nmap/scripts# ls *vuln*

Now we'll look at how we can find out what each of these scripts can do in a nutshell. However, for these scripts with the word vuln, it is helpful to know that many file names have CVE numbers associated with them. With these CVE numbers we can find out on the Internet what the issue is.

Let's take a closer look at a script

kali@kali:/usr/share/nmap/scripts# ls *smb*

kali@kali:/usr/share/nmap/scripts# sudo nmap --script-help smb-os-discovery.nse

This tells us that the script is trying to determine the operating system, computer name, domain, workgroup and current time via the SMB protocol. And, we can read a few more comments here about what we might run into with gotchas, as well as an additional help URL

Let's take a look at it right now.

kali@kali:~# sudo nmap --script=smb-os-discovery.nse -p445 192.168.93.200

kali@kali:~# sudo nmap --script=smb-os-discovery.nse -p445 192.168.93.0/24

kali@kali:~# sudo nmap --script=smb-os-discovery.nse -p445 -iL targets.txt

Let's take a look at another script.

kali@kali:~# sudo nmap --script-help banner.nse

Let's take a look at the help file for another script such as Banner NSE. And, let's open the URL for the associated help file. I want to draw your attention to a couple of things here. One is that this script is categorised under discovery and safe. Remember how we looked at scripts with names containing the words brute or vuln, by navigating around the NSE help section, you can quickly pull up a category like brute and see all the scripts that fall into that category. But what does safe mean, that can be found in the documentation and Categories. Let's take a look at the banner script, but first a 'normal' scan.

kali@kali:~# sudo nmap 192.168.93.10

kali@kali:~# sudo nmap --script=banner.nse 192.168.93.10

a little more specific

kali@kali:~# sudo nmap --script=banner.nse --script-args banner.port=53 192.168.93.10

or only for port 53

kali@kali:~# sudo nmap --script=banner.nse -p53 192.168.93.10

kali@kali:~# sudo nmap --script=banner.nse -p53 192.168.93.0/24

kali@kali:~# sudo nmap --script=banner.nse -p53 192.168.93.0/24 --open


I hope you enjoyed the tutorial and learned something new!
---

---
## *HAPPY SCANNING!*
---