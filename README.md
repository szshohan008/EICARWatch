# EICARWatch

EICARWatch is a SOC validation pipeline using the EICAR test file to simulate malware detection and alerting.

## Features
- EICAR-based safe malware simulation
- Wazuh SIEM integration
- Email & Telegram alerting
- Detection latency evaluation

## Architecture
EICAR → Endpoint → Wazuh Agent → Wazuh Manager → ELK → Alerting

## Usage
1. Run EICAR generator
2. Monitor alerts in Wazuh
3. Receive notifications via Telegram/Email
