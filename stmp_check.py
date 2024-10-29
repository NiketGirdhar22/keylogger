import smtplib

try:
    smtp_server = "smtp.gmail.com"
    smtp_port = 465
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        print("Connection successful!")
except Exception as e:
    print("Failed to connect:", e)