import pandas as pd
import datetime
import requests
import os

# --- SETTINGS ---
EXCEL_PATH = "Name.xlsx"                        # Your Excel file path
WHATSAPP_TOKEN = os.environ.get("WHATSAPP_TOKEN")    # Get from env variable
PHONE_NUMBER_ID = os.environ.get("PHONE_NUMBER_ID")  # Get from env variable
RECIPIENT_NUMBER = "+91-9861116342"                    # Recipient's WhatsApp number (international format, no '+')
COLUMNS_TO_SHOW = ["Details", "Type", "Plan", "Actual", "Date(day)", "From"]
print("WHATSAPP_TOKEN:", repr(os.environ.get("WHATSAPP_TOKEN")))
# --- READ & FILTER EXCEL ---
df = pd.read_excel(EXCEL_PATH)
today_day = datetime.datetime.now().day
yesterday_day = today_day - 1

filtered = df[df["Date(day)"] == yesterday_day]
filtered = filtered[COLUMNS_TO_SHOW]
table_str = filtered.to_string(index=False)

if filtered.empty:
    table_str = "No records found for yesterday."

# --- WHATSAPP META CLOUD API SEND ---
url = f'https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages'
headers = {
    'Authorization': f'Bearer {WHATSAPP_TOKEN}',
    'Content-Type': 'application/json',
}
data = {
    "messaging_product": "whatsapp",
    "to": RECIPIENT_NUMBER,
    "type": "text",
    "text": {
        "body": f"Auto-generated report for items dated {yesterday_day}:\n\n{table_str}"
    }
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print("Message sent successfully!")
else:
    print("Error sending message:", response.status_code, response.text)
