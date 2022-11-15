import csv

import cv2 as cv
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.layers import Input


def load_my_fancy_dataset():
    with open(r'Resources/triangles.csv') as csv_file:
        data_reader = csv.reader(csv_file)
        next(data_reader, None)
        data = []
        target = []
        i = 0
        for row in data_reader:
            i += 1
            label = row[-1]
            target.append(int(label))
            image = cv.imread(r'Resources/images/pair%i.jpg' % i)
            data.append(image)
        data = np.array(data)
        target = np.array(target)
    return data, target


def train(data, target):
    data = data / 255.0
    train_data, test_data, train_target, test_target = train_test_split(data, target, test_size=.2)

    model = keras.Sequential()
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(100, 200, 3)))
    model.add(layers.MaxPooling2D(2, 2))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D(2, 2))
    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(32, activation='relu'))
    model.add(layers.Dense(10, activation='softmax'))
    # input_tensor = Input(shape=(100, 200, 3))
    #
    # model = InceptionV3(input_tensor=input_tensor, weights='imagenet', include_top=True)
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(train_data, train_target, epochs=16, validation_data=(test_data, test_target))
