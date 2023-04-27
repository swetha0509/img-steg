import numpy as np
from PIL import Image
from tensorflow import keras

def generate_key(image_path):
    # Load the trained model
    model = keras.models.load_model('cnn_for_kgen.h5')

    # Load the cover image
    img = Image.open(image_path).convert('L')
    img = img.resize((256, 256), resample=Image.BICUBIC)
    img = np.array(img)
    cover_image = img.reshape(1, img.shape[0], img.shape[1], 1)

    # Predict the key
    key = model.predict(cover_image)

    # Reshape the output to a 1D binary array
    binary_key = np.round(key).flatten().astype(int).tolist()
    binary_key = binary_key[:128]
    key_int = int("".join(str(bit) for bit in binary_key), 2)
    key_hex = hex(key_int)

    return str(key_hex)

print(generate_key(r"C:\Users\swetha\fn_year\image-steganography\dataset\train\cover\train4.png"))