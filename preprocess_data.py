import os
import numpy as np
from PIL import Image

# define paths to training and testing sets
cover_train_dir = r'C:/Users/swetha/fn_year/image-steganography/dataset/train/cover'
key_train_dir = r'C:/Users/swetha/fn_year/image-steganography/dataset/train/keys'
cover_test_dir = r'C:/Users/swetha/fn_year/image-steganography/dataset/test/cover'
key_test_dir = r'C:/Users/swetha/fn_year/image-steganography/dataset/test/keys'

# # Set the target image size for resizing
# IMAGE_SIZE = (256, 256)

# # Load cover images and corresponding secret messages
# train_cover_images = []
# test_cover_images = []

# # Load cover images from the train directory

# for filename in os.listdir(train_dir):
#     if filename.endswith('.png'):
#         img_path = os.path.join(train_dir, filename)
#         img = Image.open(img_path)
#         img = img.resize(IMAGE_SIZE)
#         img = np.asarray(img) / 255.0  # normalize pixel values
#         train_cover_images.append(img)

# # Load cover images from the test directory

# for filename in os.listdir(test_dir):
#     if filename.endswith('.png'):
#         img_path = os.path.join(test_dir, filename)
#         img = Image.open(img_path)
#         img = img.resize(IMAGE_SIZE)
#         img = np.asarray(img) / 255.0  # normalize pixel values
#         test_cover_images.append(img)

# # Convert data to numpy arrays
# train_cover_images = np.array(train_cover_images)
# test_cover_images = np.array(test_cover_images)

# print("-",train_cover_images.shape)
# print("-",test_cover_images.shape)

# train_cover = np.save("train_cover.npy", train_cover_images)
# test_cover = np.save("test_cover.npy", test_cover_images)

# # import os
# # import numpy as np

# # # Define function to one-hot encode secret messages
# # def one_hot_encode(text):
# #     binary_repr = ''.join(['{0:08b}'.format(ord(char)) for char in text])
# #     return np.array(list(binary_repr), dtype=int)

# # # Preprocess secret messages for train directory
# # train_messages = []
# # for file_name in os.listdir(train_dir):
# #     with open(os.path.join(train_dir, file_name), 'r') as f:
# #         message = f.read().strip()
# #         train_messages.append(message)

# # # Preprocess secret messages for test directory
# # test_messages = []
# # for file_name in os.listdir(test_dir):
# #     with open(os.path.join(test_dir, file_name), 'r') as f:
# #         message = f.read().strip()
# #         test_messages.append(message)

# # max_length = 100  # Maximum length of secret message
# # train_messages_encoded = []
# # for message in train_messages:
# #     # Pad/truncate message to fixed length
# #     message = message[:max_length].ljust(max_length, '\x00')
# #     # Convert characters to ASCII codes
# #     message_ascii = np.frombuffer(message.encode('ascii'), dtype=np.uint8)
# #     # One-hot encode
# #     message_onehot = np.zeros((max_length, 256))
# #     message_onehot[np.arange(max_length), message_ascii] = 1
# #     train_messages_encoded.append(message_onehot)

# # train_messages_encoded = np.array(train_messages_encoded)
# # np.save('train_secret.npy', train_messages_encoded)

# # test_messages_encoded = []
# # for message in test_messages:
# #     # Pad/truncate message to fixed length
# #     message = message[:max_length].ljust(max_length, '\x00')
# #     # Convert characters to ASCII codes
# #     message_ascii = np.frombuffer(message.encode('ascii'), dtype=np.uint8)
# #     # One-hot encode
# #     message_onehot = np.zeros((max_length, 256))
# #     message_onehot[np.arange(max_length), message_ascii] = 1
# #     test_messages_encoded.append(message_onehot)

# # test_messages_encoded = np.array(test_messages_encoded)
# # np.save('test_secret.npy', test_messages_encoded)

# # print(test_messages_encoded.shape)
# # print(train_messages_encoded.shape)

train_cover = []
for img_name in os.listdir(cover_train_dir):
    img = Image.open(os.path.join(cover_train_dir, img_name)).convert('L')
    img = img.resize((256, 256), resample=Image.BICUBIC)
    train_cover.append(np.array(img))
train_cover = np.array(train_cover)

test_cover = []
for img_name in os.listdir(cover_test_dir):
    img = Image.open(os.path.join(cover_test_dir, img_name)).convert('L')
    img = img.resize((256, 256), resample=Image.BICUBIC)
    test_cover.append(np.array(img))
test_cover = np.array(test_cover)

train_key = []
for key_name in os.listdir(key_train_dir):
    with open(os.path.join(key_train_dir, key_name), 'rb') as f:
        key = f.read()
        key = "".join([format(x, '08b') for x in key])
        key = np.array([int(x) for x in key])
    train_key.append(key)
train_key = np.array(train_key)

test_key = []
for key_name in os.listdir(key_test_dir):
    with open(os.path.join(key_test_dir, key_name), 'rb') as f:
        key = f.read()
        key = "".join([format(x, '08b') for x in key])
        key = np.array([int(x) for x in key])
    test_key.append(key)
test_key = np.array(test_key)

print(train_cover.shape)
print(test_cover.shape)
print(train_key.shape)
print(test_key.shape)

np.save('train_cover.npy', train_cover)
np.save('train_key.npy', train_key)
np.save('test_cover.npy', test_cover)
np.save('test_key.npy', test_key)