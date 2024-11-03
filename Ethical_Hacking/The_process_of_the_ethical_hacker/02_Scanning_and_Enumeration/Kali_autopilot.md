## Kali Autopilot
The Kali Autopilot is a tool that automates the process of scanning and enumeration. It is a Python script that uses Nmap and other tools to scan and enumerate a target system. The Kali Autopilot can be used to quickly identify vulnerabilities and misconfigurations in a target system.

### Preparations:

1. **Install Kali Autopilot**:

```
sudo apt install -y kali-autopilot
```

2. **Run Kali Autopilot**:

```
kali-autopilot
```

3. **Define the stages**:

> <img src="/Images/01_KA.JPG" alt="The Attack Stages">

**Do not forget to click on the "Generate" Button to generate the script.**

4. **Change in to the directory where the script is saved**:

```
cd kali-autopilot/juicy
```

5. **Run the script**:

```
python3 juicy.py
```

> <img src="/Images/02_KA.JPG" alt="Run the Script">

6. **Open the Browser**:

http://127.0.0.1/check  (Username and Password => offsec and offsec)

> <img src="/Images/03_KA.JPG" alt="Open the Browser">

**The Stage 0 has started.**

> <img src="/Images/04_KA.JPG" alt="Open the Browser">

7. **Start the Attack**:

Change the URL as below:

http://127.0.0.1/set?mutex=1

> <img src="/Images/05_KA.JPG" alt="Change the URL">

8. **Back in the Terminal Show the Results**:

> <img src="/Images/06_KA.JPG" alt="Easter Egg">

---
## *HAPPY ATTACK!*
---