import os
import shutil
from sklearn.model_selection import train_test_split

# Define the path to the dataset directory
dataset_path = r"C:/Users/swetha.s/Downloads/archive/boss_256_0.4/cover"

# Define the paths for the training and testing directories
train_path = r"C:/Users/swetha.s/OneDrive - IDP Education Ltd/Desktop/final_yr/steganography/dataset/train/cover"
test_path = r"C:/Users/swetha.s/OneDrive - IDP Education Ltd/Desktop/final_yr/steganography/dataset/test/cover"

# Define the percentage of the data to use for testing
test_size = 0.1

# Define the maximum number of images to use
max_images = 700

# Get the list of image filenames in the dataset directory
image_filenames = [f for f in os.listdir(dataset_path) if f.endswith(".png")]

# Limit the number of images to the maximum number
image_filenames = image_filenames[:max_images]

# Split the data into training and testing sets
train_filenames, test_filenames = train_test_split(image_filenames, test_size=test_size)

# # Create the training and testing directories
# os.makedirs(train_path, exist_ok=True)
# os.makedirs(test_path, exist_ok=True)

# Copy the training images to the training directory
for filename in train_filenames:
    src_path = os.path.join(dataset_path, filename)
    dst_path = os.path.join(train_path, filename)
    shutil.copy(src_path, dst_path)

# Copy the testing images to the testing directory
for filename in test_filenames:
    src_path = os.path.join(dataset_path, filename)
    dst_path = os.path.join(test_path, filename)
    shutil.copy(src_path, dst_path)
