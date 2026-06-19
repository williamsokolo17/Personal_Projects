# Basic Network Sniffer

## Overview
The Basic Network Sniffer is a Python-based cybersecurity tool developed using the Scapy library. It captures network packets in real time and displays important information such as source IP address, destination IP address, protocol type, and packet length.

This project was completed as part of the CodeAlpha Cyber Security Internship.

## Features
- Captures live network traffic
- Displays source IP addresses
- Displays destination IP addresses
- Detects TCP and UDP protocols
- Shows packet length
- Monitors network traffic in real time

## Technologies Used
- Python 3
- Scapy
- Npcap (Windows)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/williamsokolo17/CodeAlpha_CyberSecurity
```

2. Navigate to the project directory:

```bash
cd Task1_NetworkSniffer
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the program with administrator privileges:

```bash
python network_sniffer.py
```

The program will start capturing and displaying network packets in real time.

## Sample Output

```text
============================================================
Source IP      : 192.168.1.10
Destination IP : 8.8.8.8
Protocol       : TCP
Packet Length  : 74 bytes
```

## Project Structure

```text
Task1_NetworkSniffer/
│
├── network_sniffer.py
├── requirements.txt
├── README.md
└── screenshots/
```

## Learning Outcomes

Through this project, I gained practical knowledge of:

- Network packet capture
- TCP/IP communication
- Traffic analysis
- Real-time network monitoring
- Cybersecurity fundamentals

## Disclaimer

This tool is intended for educational purposes and authorized network monitoring only. Unauthorized packet sniffing may violate laws and organizational policies.

## Author

Okolo Williams

Cybersecurity Enthusiast | SOC Analyst Learner