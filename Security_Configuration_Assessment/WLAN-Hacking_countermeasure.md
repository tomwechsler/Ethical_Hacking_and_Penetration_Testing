# Countermeasures Against WLAN Hacking: A Comparison Between Businesses and Private Households

---

| **Countermeasure**                        | **For Businesses**                                                                | **For Private Households**                                                 |
| ----------------------------------------- | --------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **Use strong encryption**                 | Use WPA3-Enterprise with RADIUS authentication                                    | Use WPA3 or at least WPA2 with a strong password                           |
| **Strong passwords**                      | Complex, regularly rotated Wi-Fi credentials with centralized password management | Strong Wi-Fi password (avoid default router passwords)                     |
| **SSID management**                       | Do not broadcast sensitive SSIDs; avoid default SSID names                        | Change SSID name (avoid names like “FritzBox123”); hiding SSID is optional |
| **Access restrictions**                   | Use MAC filtering as a supplementary measure; prefer certificate or portal access | MAC filtering can be used as an extra precaution                           |
| **Network segmentation**                  | Separate guest, IoT, and internal networks using VLANs or firewalls               | Use separate Wi-Fi for guests and smart home devices                       |
| **Centralized authentication**            | Authenticate via RADIUS, LDAP, or SAML for larger environments                    | Not applicable / impractical for home use                                  |
| **Monitoring & logging**                  | Monitor WLAN activity (e.g. via IDS/IPS or SIEM tools)                            | Check router logs and respond to signs of suspicious access                |
| **Firmware updates**                      | Regularly update firmware on access points and controllers                        | Check and update router firmware regularly (manually if needed)            |
| **Disable insecure features**             | Disable WPS, UPnP, Telnet, and other unnecessary services                         | Turn off WPS; only enable needed features                                  |
| **Avoid interference sources**            | Conduct site surveys; use professional WLAN planning tools (e.g. heatmaps)        | Position router wisely; monitor surrounding networks for interference      |
| **Secure Bluetooth and other interfaces** | Manage and protect adjacent wireless interfaces separately                        | Turn off Bluetooth and other wireless interfaces when not in use           |
| **Security awareness training**           | Educate staff on WLAN risks and social engineering                                | Provide basic Wi-Fi safety knowledge to all household members              |
| **Use VPN over WLAN**                     | Company devices should connect via VPN over Wi-Fi                                 | Use VPN when accessing sensitive data over public Wi-Fi                    |
