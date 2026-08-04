# Azure Sentinel Cloud Security Monitoring Platform

## Overview

The Azure Sentinel Cloud Security Monitoring Platform is a cybersecurity engineering project designed to monitor Azure activity, detect suspicious behavior, audit identities, and automate security analysis.

This project simulates the workflow of a cloud security engineer by integrating:

- Microsoft Sentinel
- Microsoft Entra ID
- Azure Monitor
- Python security automation
- KQL detection engineering
- GitHub Actions security scanning


# Architecture
Microsoft Entra ID
|
|
Azure Activity Logs
|
|
Azure Monitor
|
|
Microsoft Sentinel
|
|
Python Detection Engine
|
|
Security Dashboard
|
|
Security Reports



# Project Goals

This platform demonstrates enterprise cloud security practices:

## SIEM Monitoring

Technologies:

- Microsoft Sentinel
- Azure Monitor
- Kusto Query Language (KQL)

Capabilities:

- Monitor authentication events
- Detect suspicious activity
- Generate security alerts


## Cloud Identity Security

Using Microsoft Entra ID:

Implemented:

- Users
- Groups
- RBAC permissions
- MFA monitoring
- Privileged account auditing


## Detection Engineering

Custom detections include:

### Brute Force Login Detection

Detect:

- Multiple failed login attempts
- Password spraying behavior


### Privilege Escalation Detection

Detect:

- Administrator role assignments
- Unexpected permission changes


### Suspicious Login Detection

Detect:

- Unusual locations
- Abnormal authentication behavior


# Python Security Automation

Python scripts automate:

- Azure log collection
- Security event analysis
- Alert generation
- Security reports


Workflow:
Azure Logs

↓

Python Analyzer

↓

Detection Rules

↓

Security Alert

↓

Report



# Vulnerability Management

Security scanning tools:

- Bandit
- pip-audit
- Trivy

Checks:

- Vulnerable dependencies
- Unsafe Python code
- Container vulnerabilities


# Secure CI/CD Pipeline

GitHub Actions performs automated security checks:
Developer Push

↓

GitHub Actions

↓

Security Testing

↓

Bandit

↓

pip-audit

↓

Trivy

↓

Build Approva



# Technologies Used

## Cloud

- Microsoft Azure
- Microsoft Sentinel
- Azure Monitor
- Microsoft Entra ID


## Programming

- Python
- SQL


## Security

- SIEM
- IAM
- KQL
- Detection Engineering
- Vulnerability Management


## DevSecOps

- GitHub Actions
- Bandit
- Trivy
- pip-audit


# Future Improvements

- Automated incident response
- Threat intelligence integration
- Azure Functions automation
- Security dashboard
- Real-time notifications


# Author

Aslam Bwanika

Cybersecurity Engineering Portfolio Project
