# sshbruteforce.py
A Python SSH brute-forcer using Pwntools and Paramiko. Attempts each password from a wordlist against a target host and username, reporting the correct one upon success.


# 🔑 SSH Brute Force Tool

A Python-based SSH login brute-forcer built with [Pwntools](https://docs.pwntools.com/en/stable/) and [Paramiko](http://www.paramiko.org/).  
It automates password-guessing attempts against SSH services using a wordlist.

---

## 📜 Description
This script attempts to gain SSH access by systematically testing each password from a specified wordlist (`passwords.txt`) against a target host and username.  
It uses:
- **Pwntools** for streamlined SSH connections
- **Paramiko** for handling SSH exceptions gracefully

The script stops as soon as a valid password is found.

---

## 🚀 Features
- ✅ Works on any SSH-enabled host
- ✅ Real-time attempt logging
- ✅ Handles authentication exceptions
- ✅ Stops immediately after finding a valid password

---

## 🛠 Requirements
- Python 3.x
- [Pwntools](https://docs.pwntools.com/en/stable/)
- [Paramiko](http://www.paramiko.org/)

Install dependencies:
```bash
pip install pwntools paramiko

📂 Wordlist

Place your password list in the script’s directory as:

passwords.txt

Or modify the script to point to your desired wordlist path.
💻 Usage

Run the script and provide target details:

python3 sshbruteforce.py

Example:

input target: 192.168.1.100
input username: admin
[0] Attempting password: '123456' !
[X] Invalid password!
...
[17] Attempting password: 'toor' !
[>] Valid password found: toor !

📌 Notes

    Default SSH port is 22. Modify the code if targeting a different port.

    If the target blocks repeated login attempts, try adding delays.

⚠ Disclaimer

This tool is intended for educational and authorized penetration testing purposes only.
Using it against systems without permission is illegal.
