from cryptography.fernet import Fernet

key = Fernet.generate_key()
file = open('key.key', 'wb')
file.write(key)
file.close()

file = open('symmetric.key', 'rb')
key = file.read()
file.close()

with open('credentials.json', 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

with open('credentials.json', 'wb') as f:
    f.write(encrypted)
