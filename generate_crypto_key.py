# Standard library
import os
from pathlib import Path

# Third party
from cryptography.fernet import Fernet
from dotenv import load_dotenv

# Constants
CRYPTO_KEY_ENV_VAR = 'CRYPTO_KEY'
ENV_VAR_EXIST = f'The {CRYPTO_KEY_ENV_VAR} environment variable already exist.  Cannot continue as the crypto key may still be in use.'
ENV_VAR_PATH = Path.home() / '.my_python_env'

# Load virtual environmental variables
load_dotenv(dotenv_path=ENV_VAR_PATH)

def environment_var_exist():
    return os.environ.get(CRYPTO_KEY_ENV_VAR)

def generate_key():
    return Fernet.generate_key()

def write_key_env_var(crypto_key):
    # Only write if environmental variable does not exist.
    # Otherwise raise an exception - environment variable already exists.
    if not environment_var_exist():
        with ENV_VAR_PATH.open(mode='w') as file:
            file.write(f'{CRYPTO_KEY_ENV_VAR}={crypto_key}')

    else:
        raise Exception(ENV_VAR_EXIST)

if __name__ == '__main__':
    crypto_key = generate_key().decode()
    write_key_env_var(crypto_key)

