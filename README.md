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

## 📋 Prerequisites

Before running the script, ensure you have the following requirements met:
1.  **Python 3.8+**: Installed on your local machine.
2.  **Cisco Device Access**: Reachability to a Cisco IOS-XR device (e.g., via Cisco DevNet Sandbox).
3.  **VPN Connection**: An active connection (such as Cloudflare WARP) if you are accessing a remote lab environment.
4.  **Network Reachability**: Ensure you can ping the target device host from your terminal.

## ⚙️ Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
    cd YOUR_REPO_NAME
    ```

2.  **Set Up Virtual Environment**
    It is highly recommended to use a virtual environment to manage dependencies:
    ```bash
    python -m venv venv
    
    # Windows activation
    .\venv\Scripts\activate

    # Linux/MacOS activation
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    Install the required libraries using pip:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configuration**
    Create a secure environment file by copying the template:
    ```bash
    cp .env.example .env
    ```
    *Open the `.env` file and fill in your actual device credentials (Host, User, Pass, Port).*

## 🏃 Usage

Execute the automation script to start the health check:
```bash
python main.py
 ```
Upon execution, the script will:
- **Establish a Secure Connection**: Initiates an SSH session via NAPALM with the target IOS-XR device.
- **Automated Command Execution**: Systematically runs diagnostics including versioning, interface status, and inventory.
- **Data Persistence**: Automatically compiles and exports the retrieved data into timestamped **JSON** and **TXT** formats for historical tracking.
- **Session Cleanup**: Safely closes the SSH connection to ensure device resource integrity.

## 📊 Sample Output (JSON)

The tool generates a structured report that is easy to parse for further automation:
```json
{
    "timestamp": "2026-05-11 10:00:00",
    "host": "sbx-iosxr-mgmt.cisco.com",
    "results": {
        "show version": "Cisco IOS XR Software, Version 7.3.1...",
        "show ipv4 interface brief": "GigabitEthernet0/0/0/0 10.10.20.175 Up Up..."
    }
}
```
I welcome collaboration and technical discussions. If you are looking to implement similar automation in your infrastructure:

1.  Open an **Issue** for architectural discussions.
2.  Submit a **Pull Request** for feature enhancements.

---
## 🤝 Connect with Me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/annasalakram/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat&logo=github)](https://github.com/annasalakram)
[![Email](https://img.shields.io/badge/Email-Contact-red?style=flat&logo=gmail&logoColor=white)](mailto:annas.tnt@gmail.com)
