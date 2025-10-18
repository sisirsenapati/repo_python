import smtplib


def automatic_email():
    user = input("Enter Your Name >>: ")
    sender_email = input("Enter Your Gmail Address (sender) >>: ")
    app_password = input("Enter Your Gmail App Password >>: ")
    recipient_email = input("Enter Recipient Email (To) >>: ")

    subject = "Welcome to My Py World"
    body = f"Dear {user},\nWelcome to my py world"
    message = f"Subject: {subject}\nFrom: {sender_email}\nTo: {recipient_email}\n\n{body}"

    with smtplib.SMTP('smtp.gmail.com', 587) as s:
        s.starttls()
        s.login(sender_email, app_password)
        s.sendmail(sender_email, recipient_email, message)
        print("Email Sent!")


automatic_email()
