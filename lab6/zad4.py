import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
import seaborn as sns
import os
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPooling2D, Dropout
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix
from tensorflow.keras.callbacks import History
from tensorflow.keras.applications import MobileNet


# Create a dataset of images

# path = 'C:\\Users\\kamil\\Downloads\\dogs-cats-mini'
# photos, labels = list(), list()
# for file in os.listdir(path):
#     output = 0.0
#     if file.startswith('dog'):
#         output = 1.0
#     photo = load_img(path + '\\' + file, target_size=(200, 200))
#     photo = img_to_array(photo)
#     photos.append(photo)
#     labels.append(output)
# photos = np.asarray(photos)
# labels = np.asarray(labels)
# np.save('dogs_vs_cats_photos.npy', photos)
# np.save('dogs_vs_cats_labels.npy', labels)

# Load the dataset
photos = np.load('dogs_vs_cats_photos.npy')
labels = np.load('dogs_vs_cats_labels.npy')
# # print(photos.shape, labels.shape)
indices = np.arange(len(photos))
np.random.shuffle(indices)
photos = photos[indices]
labels = labels[indices]
# Split the dataset into training and test sets
train_size = int(0.75 * len(photos))
X_train, X_test = photos[:train_size], photos[train_size:]
y_train, y_test = labels[:train_size], labels[train_size:]
X_train = X_train / 255.0
X_test = X_test / 255.0
# # Define the model
# model = Sequential([
#     Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(200, 200, 3)),
#     MaxPooling2D(pool_size=(2, 2)),
#     Dropout(0.25),
#     Conv2D(64, kernel_size=(3, 3), activation='relu'),
#     MaxPooling2D(pool_size=(2, 2)),
#     Dropout(0.25),
#     Flatten(),
#     Dense(64, activation='relu'),
#     Dense(1, activation='sigmoid')
# ])
base_model = MobileNet(weights='imagenet', include_top=False, input_shape=(200, 200, 3))
base_model.trainable = False

model = Sequential([
    base_model,
    Flatten(),
    Dense(256, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')
])

# # Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


# # Train the model
history = model.fit(X_train, y_train, epochs=5, validation_split=0.2)

# # Evaluate the model on the test set
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Test Accuracy: {test_accuracy*100:.2f}%")

# Plot the learning curve
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='train accuracy')
plt.plot(history.history['val_accuracy'], label='validation accuracy')
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.grid(True, linestyle='--', color='grey')
plt.legend()
## dropotu - losowe wyłączanie neuronów
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='train loss')
plt.plot(history.history['val_loss'], label='validation loss')
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.grid(True, linestyle='--', color='grey')
plt.legend()

plt.tight_layout()
plt.show()

# Save the model
# model.save('dogs_vs_cats_model.h5')

