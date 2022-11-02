import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
import sqlite3
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

conn = sqlite3.connect('database.db')
password = input('password: ').encode('utf_8')
salt = os.urandom(16)
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA512(),
    length=32,
    salt=salt,
    iterations=390000,
)
key = base64.urlsafe_b64encode(kdf.derive(password))
print(key)
f = Fernet(key)
token = f.encrypt(b"Secret message!")
print(token)
f.decrypt(token)