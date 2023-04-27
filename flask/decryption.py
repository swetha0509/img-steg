# 4. decryption

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

# Convert the hex key to a byte string

def decrypt_text(data, key):
    key = bytes.fromhex(key)

    # Read the encrypted ciphertext and IV from the file

    ciphertext_b64 = data

    print(ciphertext_b64)
    # Decode the Base64-encoded ciphertext to binary data
    ciphertext = base64.b64decode(ciphertext_b64)

    # Extract the IV and ciphertext from the binary data
    iv = ciphertext[:16]
    ciphertext = ciphertext[16:]

    # Create an AES cipher object with the key and IV
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    # Decrypt the ciphertext using the cipher object
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # Remove any null bytes that were added for padding
    plaintext = plaintext.rstrip(b'\0')

    # Print the decrypted plaintext
    print("Decrypted plaintext:")
    return plaintext.decode('utf-8')

