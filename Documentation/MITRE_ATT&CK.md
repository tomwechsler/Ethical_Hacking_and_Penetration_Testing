# What is the MITRE ATT&CK Framework and the Tactics, Techniques, and Procedures (TTPs)?

Cybersecurity is an ever-evolving field where understanding attacker behavior is critical to defending against threats. The **MITRE ATT&CK Framework** is one of the most valuable tools in the cybersecurity professional’s arsenal. This article delves into what the MITRE ATT&CK Framework is, explores the concept of **Tactics, Techniques, and Procedures (TTPs)**, and explains their relationship through the lens of a web application attack.

---

## What is the MITRE ATT&CK Framework?

The **MITRE ATT&CK Framework** is a globally-accessible knowledge base that documents and categorizes adversary behavior in the context of cybersecurity. It stands for **Adversarial Tactics, Techniques, and Common Knowledge**, focusing on how attackers operate across various stages of an attack lifecycle.

Key features of the framework include:

1. **Tactics**: High-level objectives attackers aim to achieve during their campaigns.
2. **Techniques**: The methods attackers use to achieve their objectives.
3. **Procedures**: Specific implementations or variations of techniques observed in real-world attacks.

The framework is widely used by organizations to:

- Improve threat detection capabilities.
- Enhance incident response.
- Develop defensive strategies.
- Understand and emulate adversary behavior through red teaming.

---

## Understanding Tactics, Techniques, and Procedures (TTPs)

The concept of **TTPs** breaks down attacker behavior into granular components, enabling defenders to identify patterns and predict potential threats. 

### 1. **Tactics**
Tactics represent the “why” behind an attack. They define the adversary's goals, such as gaining initial access, maintaining persistence, or exfiltrating data. Examples include:

- Initial Access
- Execution
- Privilege Escalation
- Data Exfiltration

### 2. **Techniques**
Techniques describe the “how.” These are specific actions or methodologies attackers use to achieve their goals. For example, under the tactic of “Initial Access,” techniques could include:

- **Phishing** (T1566): Sending malicious emails to gain access.
- **Exploit Public-Facing Applications** (T1190): Exploiting vulnerabilities in web applications.

### 3. **Procedures**
Procedures are the “what” in terms of implementation. They are the specific tools or methods attackers use to execute a technique. For instance, using the **SQLMap tool** to exploit SQL injection vulnerabilities in a web application would be an example of a procedure.

---

## From General to Specialized: Example of a Web Application Attack

To understand the connection between TTPs, let's explore a web application attack scenario. 

### Tactic: Initial Access
The attacker’s goal is to gain unauthorized access to the web application. 

- **Technique**: Exploit Public-Facing Application (T1190)  
  The adversary identifies and exploits a vulnerability in the web application.

- **Procedure**: SQL Injection  
  The attacker uses a specialized tool like SQLMap to exploit an input field in the web application that fails to sanitize user input properly.

### Tactic: Persistence
After gaining access, the attacker wants to ensure ongoing access.

- **Technique**: Create or Modify Account (T1136)  
  The attacker creates a hidden admin account in the application.

- **Procedure**: Exploiting an administrative panel to create a backdoor user with elevated privileges.

### Tactic: Data Exfiltration
The final goal is to steal sensitive data.

- **Technique**: Data Transfer Size Limits (T1030)  
  The attacker uses chunked file uploads to avoid detection by network monitoring tools.

- **Procedure**: Writing custom scripts to exfiltrate sensitive user data in small, encrypted chunks.

---

<img src="/Images/mitre_ttps.png" alt="Tactics, Techniques, and Procedures (TTPs)">

---

## Benefits of the TTP-Based Approach

1. **Granular Understanding**  
   By categorizing attacks into TTPs, defenders can analyze each stage of an attack lifecycle and implement targeted defenses.

2. **Threat Intelligence**  
   Mapping real-world threats to TTPs helps organizations understand emerging threats and prepare accordingly.

3. **Improved Collaboration**  
   The framework provides a common language for red and blue teams, improving incident detection and response.

---

## Leveraging the MITRE ATT&CK Framework

Organizations can leverage the MITRE ATT&CK Framework to bolster their defenses:

1. **Threat Hunting**  
   Use TTPs to proactively search for malicious activity in your environment.

2. **Detection Engineering**  
   Develop detection rules for known techniques using tools like SIEMs or EDR solutions.

3. **Security Testing**  
   Red teams can emulate adversary behavior mapped to the framework to identify vulnerabilities.

4. **Training and Awareness**  
   The framework serves as an educational tool for security teams to understand attacker behavior.

---

## Conclusion

The MITRE ATT&CK Framework provides a structured and comprehensive approach to understanding adversary behavior. By focusing on **Tactics, Techniques, and Procedures (TTPs)**, organizations can break down attacker goals into manageable components, enabling effective detection, response, and prevention strategies. 

Using examples like a web application attack, it’s evident how TTPs transition from general objectives (tactics) to specific actions (procedures). By adopting the MITRE ATT&CK Framework, organizations can stay ahead of the curve in the fight against cyber threats.

---

> Source: [MITRE ATT&CK Framework](https://attack.mitre.org/)