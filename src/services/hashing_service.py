from argon2 import PasswordHasher

def encrypt_master(master_password):
    ph = PasswordHasher()
    return ph.hash(master_password)

def verify_master(hashed_master_password, master_password):
    try:
        ph = PasswordHasher()
        ph.verify(hashed_master_password, master_password)
        return True
    except:
        return False
