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
    # DevNet IOS XE on CSR 16.9.3 always on sandbox
        # device = {
        #     'device_type': 'cisco_ios',
        #     'ip': 'ios-xe-mgmt.cisco.com',
        #     'username': 'developer',
        #     'password': 'C1sco12345',
        #     'port': '8181',
        # }

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


    # Had to add the following to users ssh config file ~/.ssh/config:
    #
    #    Host ios-xe-mgmt.cisco.com
    #    KexAlgorithms=+diffie-hellman-group-exchange-sha1,diffie-hellman-group14-sha1
    #
    # otherwise the connection would fail due to no matching key exchanged method found.

    cli_output = device_connection.send_command('show ip interface brief')

    print(cli_output)

    device_connection.disconnect()



if __name__ == '__main__':
    main()

