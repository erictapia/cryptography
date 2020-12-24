# Standard Library
import json
import os
from pathlib import Path

# Third party
from netmiko import Netmiko
from cryptography.fernet import Fernet
from dotenv import load_dotenv

# Constants
CRYPTO_KEY_ENV_VAR = 'CRYPTO_KEY'
ENV_VAR_PATH = Path.home() / '.my_python_env'
CREDENTIAL_PATH = Path('.') / 'credentials' / 'ios-xe-mgmt.cisco.com.encrypted'

# Load virtual environment variables
load_dotenv(dotenv_path=ENV_VAR_PATH)

def get_key_env_var():
    return os.environ.get(CRYPTO_KEY_ENV_VAR)

def decrypt_file(src, key):
    # Load encrypted data
    with open(src, 'rb') as file:
        encrypted_data = file.read()
    
    # decrypt data
    fern = Fernet(key)
    data = fern.decrypt(encrypted_data)

    return data

def main():
    key = get_key_env_var()
    data = decrypt_file(CREDENTIAL_PATH, key.encode()).decode()

    device = json.loads(data)

    device_connection = Netmiko(**device)

    cli_output = device_connection.send_command('show ip interface brief')

    print(cli_output)

    device_connection.disconnect()



if __name__ == '__main__':
    main()

