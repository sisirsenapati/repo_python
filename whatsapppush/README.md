# WhatsApp Excel Notifications
This Python project reads an Excel file of scheduled financial or personal items, filters entries for "yesterday", and sends a formatted table of those entries to a specified WhatsApp number using Meta’s WhatsApp Cloud API.

## Features
Reads data from an Excel file (MonthPlan.xlsx)

Filters for entries where the "Date(day)" column matches yesterday’s day

Sends the results as a formatted table to a WhatsApp number via Meta Cloud API

## Prerequisites
Python 3.8+

1. A valid Meta WhatsApp Cloud API token2. 
2. WhatsApp phone number ID and recipient phone number (international format)
3. Excel file (Name.xlsx) with columns:
4. Details, Type, Plan, Actual, Date(day), From

## Installation
Clone the repository:
bash
git clone https://github.com/<your-username>/whatsapp-excel-notifications.git
cd whatsapp-excel-notifications
Install dependencies:
bash
pip install pandas openpyxl requests
Configuration
Set your Meta WhatsApp API credentials as environment variables:

Windows CMD:

text
set WHATSAPP_TOKEN=your_actual_token
set PHONE_NUMBER_ID=your_actual_phone_number_id
Or in your IDE launch configuration if running from PyCharm, VS Code, etc.

Usage
Place the MonthPlan.xlsx file in the project directory.

Run the main script:

bash
python WhatAppNoti.py
The script will:

Parse the Excel file

Filter for yesterday’s entries

Send the formatted report to the configured WhatsApp number


## Troubleshooting
401 OAuthException: Check if your token is valid, set correctly, and not expired

Environment Variable Issues: Ensure you set variables in the same shell session as where you run Python, or configure in your IDE