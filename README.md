# 🚀 Cisco IOS-XR Network Health Check Automation

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Cisco](https://img.shields.io/badge/cisco-ios--xr-orange.svg)
![Library](https://img.shields.io/badge/library-NAPALM-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

An automated network tool designed to perform comprehensive health checks on **Cisco IOS-XR** devices. This project demonstrates **Infrastructure-as-Code (IaC)** principles by automating data collection, ensuring network consistency, and reducing manual monitoring efforts.

---

## 🌟 Key Features

* **Automated Diagnostics**: Retrieves critical data including `show version`, `show ipv4 interface brief`, and `show inventory`.
* **Dual Reporting**: Generates results in both **JSON** (for system integration) and **TXT** (for human review).
* **Production-Ready Logic**: Features robust error handling, session management, and custom connection timeouts.
* **Secure Credential Management**: Integrated with `python-dotenv` to ensure sensitive information never enters the version control.

## 🛠️ Tech Stack

* **Language:** Python 3.8+
* **Network Library:** [NAPALM](https://napalm.readthedocs.io/)
* **Environment Management:** `python-dotenv`
* **Platform:** Cisco IOS-XR (Tested on Cisco DevNet Sandbox)

## 📂 Project Structure

```text
├── main.py              # Main automation script
├── .env.example         # Template for environment variables
├── .gitignore           # Ensures security by ignoring sensitive files
├── requirements.txt     # List of required Python libraries
└── README.md            # Project documentation

