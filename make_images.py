import csv
from PIL import Image, ImageDraw
import os
import glob
import re


# clears all images from the images folder, used to keep things tidy
def clear_images():
    path = r'Resources/images/*.jpg'
    files = glob.glob(path)
    for f in files:
        os.remove(f)


# function to make a jpg of a triangle given 3 sets of coordinates and save it to a folder
def triangle(output_path, r):
    image = Image.new("RGB", (200, 100), "white")
    draw = ImageDraw.Draw(image)
    draw.polygon(((int(r[0]), int(r[1])), (int(r[2]), int(r[3])), (int(r[4]), int(r[5]))), outline="black")
    draw.polygon(((int(r[6]) + 100, int(r[7])), (int(r[8]) + 100, int(r[9])), (int(r[10]) + 100, int(r[11]))), outline="black")
    draw.line(((100, 0), (100, 100)), fill='black')
    image.save(output_path)


# convert a csv of coordinates into jpgs using triangle, idk how the 'congruent' column will be used
def csv_to_images(path):
    clear_images()
    with open(path) as file:
        reader = csv.reader(file, delimiter=',')
        c = 0
        for row in reader:
            if c != 0:
                triangle(r'Resources/images/pair%i.jpg' % c, row)
            c += 1


def split_string(s):
    s1 = s[1:len(s)-1]
    indexes_left = [x.start() for x in re.finditer('\[', s1)]
    indexes_right = [x.start() for x in re.finditer('\]', s1)]
    list = []
    for i in range(0, len(indexes_right)):
        s2 = s1[indexes_left[i]+1:indexes_right[i]]
        coord_string = s2.split(', ')
        for i in coord_string:
            list.append(int(i))

    return list


def csv_to_images2(path):
    clear_images()
    reg = '\\[(\\[.*\\])*\\]'
    with open(path) as file:
        reader = csv.reader(file, delimiter=',')
        c = 0
        for row in reader:
            if c != 0:
                s1 = split_string(row[0])
                s2 = split_string(row[1])
                shape(r'Resources/images/pair%i.jpg' % c, s1, s2)
            c += 1


def shape(output_path, l1, l2):
    image = Image.new("RGB", (224, 224), "white")
    draw = ImageDraw.Draw(image)
    if len(l1) == 6:
        draw.polygon(((l1[0] + 6, l2[1] + 62), (l1[2] + 6, l1[3] + 62), (l1[4] + 6, l1[5] + 62)), outline="black")
    if len(l1) == 8:
        draw.polygon(((l1[0] + 6, l2[1] + 62), (l1[2] + 6, l1[3] + 62), (l1[4] + 6, l1[5] + 62),
                      (l1[6] + 6, l1[7] + 62)), outline="black")

    if len(l2) == 6:
        draw.polygon(((l2[0]+ 118, l2[1] + 62), (l2[2] + 118, l2[3] + 62), (l2[4] + 118, l2[5] + 62)), outline="black")
    if len(l2) == 8:
        draw.polygon(((l2[0]+ 118, l2[1] + 62), (l2[2] + 118, l2[3] + 62), (l2[4] + 118, l2[5] + 62),
                                                                           (l2[6] + 118, l2[7] + 62)),
                     outline="black")
    draw.line(((112, 0), (112, 224)), fill='black')
    image.save(output_path)


csv_to_images(r'Resources/triangles.csv')
