import csv

import cv2 as cv
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split


def load_my_fancy_dataset():
    with open(r'resources/triangles.csv') as csv_file:
        data_reader = csv.reader(csv_file)
        next(data_reader, None)
        data = []
        target = []
        i = 0
        for row in data_reader:
            i += 1
            label = row[-1]
            target.append(int(label))
            image = cv.imread(r'resources/images/pair%i.jpg' % i)
            data.append(image)
        data = np.array(data)
        target = np.array(target)
    return data, target


def train(data, target):
    data = data / 255.0
    train_data, test_data, train_target, test_target = train_test_split(data, target, test_size=.2)

    model = keras.Sequential()
    model.add(layers.Conv2D(16, (3, 3), activation='relu', input_shape=(300, 700, 3)))
    model.add(layers.MaxPooling2D(2, 2))
    model.add(layers.Flatten())
    model.add(layers.Dense(16, activation='relu'))
    model.add(layers.Dense(5, activation='softmax'))
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    model.fit(train_data, train_target, epochs=5, validation_data=(test_data, test_target))
