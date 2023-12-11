from cryptography.fernet import Fernet
key = Fernet.generate_key()
fernet = Fernet(key)

def encrypt(data):
    return fernet.encrypt(data.encode())

def decrypt(data_enc) :   
    return fernet.decrypt(data_enc).decode()
