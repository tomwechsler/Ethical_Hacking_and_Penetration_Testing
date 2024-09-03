## Common Metasploit Terminology

**Metasploit Framework (MSF)**: A software platform that is used for developing, testing, and executing exploit code against a remote target machine. It is a sub-project of the Metasploit Project.

**Exploit**: A piece of software, a chunk of data, or a sequence of commands that takes advantage of a bug, glitch, or vulnerability in order to cause unintended or unanticipated behavior to occur on computer software, hardware, or something electronic (usually computerized). This frequently includes such things as gaining control of a computer system, allowing privilege escalation, or a denial of service attack.

**Payload**: The component of an exploit that performs the malicious action. It can be a piece of code that is executed on the target system, such as a reverse shell or a meterpreter session.

**Module**: A self-contained piece of code that can be used to extend the functionality of the Metasploit Framework. Modules can be used to perform various tasks, such as scanning, exploiting, or post-exploitation activities.

**Auxiliary Module**: A module that performs a specific task, such as scanning for vulnerabilities or gathering information, but does not exploit a target system.

**Post Module**: A module that is used to perform actions on a target system after exploitation has occurred. This can include tasks such as privilege escalation, data exfiltration, or lateral movement.

**Payload Module**: A module that contains the payload code that is executed on the target system after exploitation has occurred. This can include reverse shells, meterpreter sessions, or other types of payloads.

**Exploit Module**: A module that contains the code that is used to exploit a vulnerability on a target system. This can include remote code execution, privilege escalation, or denial of service exploits.

**Listener**: A component of the Metasploit Framework that waits for incoming connections from exploited systems. Listeners are used to establish a communication channel between the attacker and the target system.

**Session**: A connection between the attacker and the target system that is established after successful exploitation. Sessions can be used to interact with the target system, run commands, and exfiltrate data.

**Meterpreter**: An advanced, dynamically extensible payload that is used in the Metasploit Framework. Meterpreter provides a wide range of functionality, including file system access, process manipulation, and network communication.

**Stager**: A small piece of code that is used to download and execute a larger payload on a target system. Stagers are used to minimize the size of the initial exploit code and to evade detection.

**Shellcode**: A small piece of code that is used to spawn a shell on a target system. Shellcode is typically written in assembly language and is used to execute commands on the target system.

**Staged Payload**: A payload that is delivered in multiple stages, with an initial stager that downloads and executes a larger payload. Staged payloads are used to evade detection and to minimize the size of the initial exploit code.

## Common Metasploit Commands

**msfconsole**: The main command-line interface for the Metasploit Framework. It is used to interact with the various modules, payloads, and exploits available in the framework.

**use**: A command used to select a module for use in the current session. For example, `use exploit/windows/smb/ms17_010_eternalblue`.

**set**: A command used to set options for the selected module. For example, `set RHOSTS`.

**show options**: To display the available options for the selected module.

**exploit**: To execute the selected module and exploit the target system.

**run**: To execute the selected module or payload same as "exploit".

**sessions**: List the active sessions that have been established with target systems.

**sessions -i <session_id>**: To interact with a specific session.

**background**: A command used to background the current session and return to the main Metasploit console.

**search**: To search for modules, payloads, or exploits in the Metasploit Framework.

**help**: To display help information for the available commands in the Metasploit Framework.

**exit**: A command used to exit the Metasploit Framework.

**db_nmap**: To import the results of an nmap scan into the Metasploit database.

**creds**: To display the credentials that have been captured during exploitation.

**vulns**: A command used to display the vulnerabilities that have been identified during exploitation.

**services**: To display the services that are running on the target system.

**hosts**: To display the hosts that have been identified during exploitation.