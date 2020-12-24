# cryptography
Learning how to encrypt and decrypt a file.  Lacks validation and used as a PoC.  Not meant for production usasge.

# Environment
Python 3.7.6
OS X

# Requirments:
cryptography - used to create key, encrypt, and decrypt file
python-dotenv - allows virtual environments to use persistent environment variables
netmiko - used to connect to a device via ssh

# Setting up environment
git clone https://www.github.com/erictapia/cryptography.git
cd cryptography
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Creating the key
python generate_crypto_key.py

# Encrypting the credential file
python encrypt_file.py

# Running 'show ip int brief' on Cisco's always on sandbox
python show_ip_int_brief.py


# Output should look like the following (if connection does not timeout):
```
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       10.10.20.48     YES NVRAM  up                    up      
GigabitEthernet2       10.255.255.3    YES other  up                    up      
GigabitEthernet3       unassigned      YES NVRAM  administratively down down    
Loopback21             unassigned      YES unset  up                    up      
Loopback25             unassigned      YES unset  up                    up      
Loopback123            unassigned      YES unset  up                    up  
```