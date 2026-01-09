# Email Sender for New Hires (Python Automation)

## Overview

This script automates the process of sending personalized emails to new hires using data stored in an Excel file (`NewHireEmail.xlsx`).  
Each recipient receives tailored information such as credentials or onboarding details.

Emails are sent via Gmail SMTP using an App Password for secure authentication.

---

## Features

- Reads new hire info from Excel
- Sends personalized emails automatically
- Uses Gmail SMTP with secure authentication
- Supports individual iteration per user
- Simple and configurable

---

## Requirements

### Python Version
- Python 3.8+

### Dependencies

| Package | Purpose |
|---------|---------|
| pandas | Reading Excel file |
| openpyxl | Excel engine |
| smtplib | SMTP handling |
| email.mime | Email formatting |

Install dependencies:

```bash
pip install pandas openpyxl
