import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
import matplotlib.pyplot as plt
import numpy as np

mnist = tf.keras.datasets.mnist

(image_train, label_train), (image_test, label_test) = mnist.load_data()

print("Trian Image shape: ", image_train.shape)
print("Train Labe: ", label_train, "\n")
print(image_train[0])

NUM = 20
plt.figure(figsize=(15, 15))
for idx in range(NUM):
    sp = plt.subplot(5, 5, idx + 1)
    plt.imshow(image_train[idx])
    plt.title(f'Label: {label_train[idx]}')
plt.show()

model = Sequential([
    Flatten(),
    Dense(512, activation='sigmoid'),
    Dense(128, activation='sigmoid'),
    Dense(64,  activation='sigmoid'),
    Dense(10,  activation='softmax'),
], name="Simple-ANN")

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy'],
)

model.fit(image_train, label_train,
          epochs=10, batch_size=10)
model.summary()
model.save('ANN_mnist.h5')

NUM = 5
predict = model.predict(image_test[0:NUM])
print(predict)

print(" * Prediction,", np.argmax(predict, axis=1))

plt.figure(figsize=(15, 15))
for idx in range(NUM):
    sp = plt.subplot(1, 5, idx+1)
    plt.imshow(image_test[idx])
plt.show()
