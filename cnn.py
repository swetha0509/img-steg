# import tensorflow as tf
# from tensorflow import keras
# import numpy as np

# # Load data
# train_cover = np.load('train_cover.npy')
# test_cover = np.load('test_cover.npy')
# train_key = np.load('train_key.npy')
# test_key = np.load('test_key.npy')

# # Preprocessing
# train_cover = train_cover.reshape(train_cover.shape[0], train_cover.shape[1], train_cover.shape[2], 1)
# test_cover = test_cover.reshape(test_cover.shape[0], test_cover.shape[1], test_cover.shape[2], 1)
# train_key = train_key.reshape(train_key.shape[0], 16, 22, 1)
# test_key = test_key.reshape(test_key.shape[0], 16, 22, 1)

# # Build model
# model = keras.Sequential([
#     keras.layers.Conv2D(16, (3,3), activation='relu', input_shape=train_cover.shape[1:]),
#     keras.layers.MaxPooling2D((2,2)),
#     keras.layers.Conv2D(32, (3,3), activation='relu'),
#     keras.layers.MaxPooling2D((2,2)),
#     keras.layers.Flatten(),
#     keras.layers.Dense(16*22, activation='sigmoid'),
#     keras.layers.Reshape((16, 22, 1))
# ])

# # Compile model
# model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

# # Train model
# model.fit(train_cover, train_key, epochs=15, validation_data=(test_cover, test_key))

import tensorflow as tf
from tensorflow import keras
import numpy as np

# Load data
train_cover = np.load('train_cover.npy')
test_cover = np.load('test_cover.npy')
train_key = np.load('train_key.npy')
test_key = np.load('test_key.npy')

# Preprocessing
train_cover = train_cover.reshape(train_cover.shape[0], train_cover.shape[1], train_cover.shape[2], 1)
test_cover = test_cover.reshape(test_cover.shape[0], test_cover.shape[1], test_cover.shape[2], 1)
train_key = train_key.reshape(train_key.shape[0], 16, 22, 1)
test_key = test_key.reshape(test_key.shape[0], 16, 22, 1)

# Build model
model = keras.Sequential([
    keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=train_cover.shape[1:]),
    keras.layers.MaxPooling2D((2,2)),
    keras.layers.Conv2D(64, (3,3), activation='relu'),
    keras.layers.MaxPooling2D((2,2)),
    keras.layers.Conv2D(128, (3,3), activation='relu'),
    keras.layers.MaxPooling2D((2,2)),
    keras.layers.Flatten(),
    keras.layers.Dense(512, activation='relu'),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(256, activation='relu'),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(16*22, activation='sigmoid'),
    keras.layers.Reshape((16, 22, 1))
])

# Compile model
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

# Train model
model.fit(train_cover, train_key, epochs=50, validation_data=(test_cover, test_key))

model.save("cnn_for_kgen.h5")