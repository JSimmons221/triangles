import csv
from PIL import Image, ImageDraw
import os
import glob


#function to make a jpg of a triangle given 3 sets of coordinates and save it to a folder
def triangle(output_path, r):
    image = Image.new("RGB", (112, 112), "white")
    draw = ImageDraw.Draw(image)
    draw.polygon(((int(r[0]) + 3, int(r[1]) + 31), (int(r[2]) + 3, int(r[3]) + 31), (int(r[4]) + 3, int(r[5]) + 31)), outline="black")
    draw.polygon(((int(r[6]) + 59, int(r[7]) + 31), (int(r[8]) + 59, int(r[9]) + 31), (int(r[10]) + 59, int(r[11]) + 31)), outline="black")
    draw.line(((59, 0), (59, 112)), fill='black')
    image.save(output_path)


#clears all images from the images folder, used to keep things tidy
def clear_images():
    path = r'Resources/images/*.jpg'
    files = glob.glob(path)
    for f in files:
        os.remove(f)


#convert a csv of coordinates into jpgs using triangle, idk how the 'congruent' column will be used
def csv_to_images(path):
    clear_images()
    with open(path) as file:
        reader = csv.reader(file, delimiter=',')
        c = 0
        for row in reader:
            if c != 0:
                triangle(r'Resources/images/pair%i.jpg' % c, row)
            c += 1


csv_to_images(r'Resources/triangles.csv')
