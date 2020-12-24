# Standard Library
import json
import os
from pathlib import Path

# Third party
from cryptography.fernet import Fernet
from dotenv import load_dotenv

CRYPTO_KEY_ENV_VAR = 'CRYPTO_KEY'
ENV_VAR_PATH = Path.home() / '.my_python_env'
SOURCE_CREDENTIAL_PATH = Path('.') / 'credentials' / 'ios-xe-mgmt.cisco.com.txt'
DESTINATION_CREDENTIAL_PATH = Path('.') / 'credentials' / 'ios-xe-mgmt.cisco.com.encrypted'

# Load virtual environment variables
load_dotenv(dotenv_path=ENV_VAR_PATH)

def get_key_env_var():
    return os.environ.get(CRYPTO_KEY_ENV_VAR)

def encrypt_file(src, dest, key):
    # Read text file
    with open(src, "rb") as file:
        file_data = file.read()
    
    # Encrypt data
    fern = Fernet(key)
    encrypted_data = fern.encrypt(file_data)

    # Write encrypted data to file
    with open(dest, 'wb') as file:
        file.write(encrypted_data)

if __name__ == '__main__':
    key = get_key_env_var()
    encrypt_file(SOURCE_CREDENTIAL_PATH, DESTINATION_CREDENTIAL_PATH, key.encode())
