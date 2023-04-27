from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import io
import base64

def encrypt_text(data, key):
    # Convert the hex key to a byte string
    #key = bytes.fromhex(key)

    # create a multiline string
    plaintext_string = data

    # convert the string to a binary stream using the io.BytesIO class
    plaintext_stream = io.BytesIO(plaintext_string.encode('utf-8'))

    # read the binary stream into a bytes object
    plaintext = plaintext_stream.read()

    # print the bytes object
    print(plaintext)

    # Pad the plaintext with null bytes to a multiple of 16 bytes (required by AES)
    missing_bytes = 16 - len(plaintext) % 16
    plaintext = plaintext + (b'\0' * missing_bytes)

    # Generate a random IV
    iv = os.urandom(16)

    # Create an AES cipher object with the key and IV
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    # Encrypt the plaintext using the cipher object
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    # Convert the binary ciphertext to a Base64-encoded string
    ciphertext_b64 = base64.b64encode(iv + ciphertext).decode('utf-8')
    print("File encrypted successfully!")

    # Write the encrypted ciphertext and IV to a new file
    return ciphertext_b64
