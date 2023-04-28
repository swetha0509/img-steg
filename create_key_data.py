import os
from cryptography.fernet import Fernet

# Define the number of keys to generate
num_keys = 601

# Generate and save the keys
for i in range(1, num_keys):
    # Generate a new AES key
    key = Fernet.generate_key()
    
    # Save the key to a file
    filename = f"key_{i}.txt"
    with open(filename, "wb") as key_file:
        key_file.write(key)