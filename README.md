
# Keylogger with Encryption and Email Notification

This project implements a keylogger using Python, which captures keystrokes, encrypts them, and periodically sends them via email. The program encrypts keystroke logs using symmetric encryption (Fernet) and securely transfers them to a specified email address. 

## Table of Contents
- [Features](#features)
- [Setup](#setup)
- [Requirements](#requirements)
- [Configuration](#configuration)
- [Usage](#usage)
  - [Starting the Keylogger](#starting-the-keylogger)
  - [Decrypting Keystrokes](#decrypting-keystrokes)
  - [Checking SMTP Connection](#checking-smtp-connection)
  - [Testing Email Logs](#testing-email-logs)
- [Notes](#notes)
- [Disclaimer](#disclaimer)

---

## Features
- **Keystroke Logging**: Captures keystrokes, including special keys, and timestamps each entry.
- **Encryption**: Encrypts logs using Fernet symmetric encryption to protect captured data.
- **Email Notification**: Sends the encrypted keystroke log via email every 60 seconds.
- **Decryption Tool**: Allows decryption of stored logs for review.

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/keylogger.git
   cd keylogger
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
   
3. [Enable less secure app access](https://myaccount.google.com/lesssecureapps) in your Google account for the email sender.

## Requirements
- Python 3.6+
- Required libraries:
  - `pynput`
  - `cryptography`
  - `smtplib`

## Configuration
1. Open `test_1.py` and `maillogs.py`.
2. Update the following fields with your email details:
   ```python
   sender_email = "your-email@gmail.com"
   receiver_email = "receiver-email@gmail.com"
   email_password = "your-password"
   ```
3. (Optional) Update the email schedule time in seconds within the `schedule_email()` function in `test_1.py`.

## Usage

### Starting the Keylogger
To start capturing keystrokes and receiving logs by email:
```bash
python test_1.py
```

### Decrypting Keystrokes
To view the captured and encrypted keystrokes:
1. Ensure the `encryption.key` and `encrypted_keystrokes.txt` files are in the directory.
2. Run the decryption script:
   ```bash
   python decrypt.py
   ```
   
### Checking SMTP Connection
To test the email server connection:
```bash
python stmp_check.py
```

### Testing Email Logs
To manually send a test email with the current log file:
```bash
python maillogs.py
```

## Notes
- Logs are encrypted and stored in `encrypted_keystrokes.txt`.
- Encryption keys are saved in `encryption.key`. Keep this file secure as it’s necessary for decryption.
- Email logging is set to every 60 seconds but can be adjusted in `schedule_email()`.

## Disclaimer
This code is intended for educational purposes only. Use responsibly and only on systems and networks where you have permission. Unauthorized keylogging or data collection without consent is illegal and punishable by law.
