import os
import base64
from argon2 import PasswordHasher
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class HashingService:
    def __init__(self):
        self.master_password = None

    def set_master_password(self, master_password):
        self.master_password = master_password

    def encrypt_master(self, master_password):
        ph = PasswordHasher()
        return ph.hash(master_password)

    def verify_master(self, hashed_master_password, master_password):
        self.set_master_password(master_password)
        try:
            ph = PasswordHasher()
            ph.verify(hashed_master_password, master_password)
            return True
        except:
            return False

    def create_salt(self):
        return os.urandom(16)

    def kdf(self, salt):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=390000,
        )
        key = base64.urlsafe_b64encode(
            kdf.derive(self.master_password.encode()))
        return Fernet(key)

    def decrypt_login_password(self, encrypted_login_password, salt):
        f = self.kdf(salt)
        return f.decrypt(encrypted_login_password)

    def encrypt_login_password(self, login):
        f = self.kdf(login.salt)
        return f.encrypt(login.password.encode())


hashing_service = HashingService()
