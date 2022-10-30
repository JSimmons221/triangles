import csv

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import datasets, layers, models
from sklearn.model_selection import train_test_split
from sklearn import neighbors, metrics, svm
from PIL import Image


def load_my_fancy_dataset():
    with open(r'resources/triangles.csv') as csv_file:
        data_reader = csv.reader(csv_file)
        feature_names = next(data_reader)[:-1]
        data = []
        target = []
        i = 0
        for row in data_reader:
            i += 1
            label = row[-1]
            target.append(int(label))
            image = cv.imread(r'resources/images/pair%i.jpg' % i)
            data.append(np.asarray(image))
        data = np.array(data)
        target = np.array(target)
    return data, target


def train(data, target):
    data = data / 255
    train_data, test_data, train_target, test_target = train_test_split(data, target, test_size=.10)

    model = models.Sequential()
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(2, 300, 300, 3)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu', ))
    model.add(layers.Conv2D(64, (3, 3), activation='relu', ))
    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(10, activation='softmax'))
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    model.fit(train_data, train_target, epochs=10, validation_data=(test_data, test_target))
