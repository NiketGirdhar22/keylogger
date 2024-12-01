from cryptography.fernet import Fernet

with open("encryption.key", "rb") as key_file:
    key = key_file.read()
fernet = Fernet(key)

with open("encrypted_keystrokes.txt", "rb") as f:
    encrypted_data = f.readlines()
for line in encrypted_data:
    decrypted_data = fernet.decrypt(line).decode()
    print(decrypted_data)