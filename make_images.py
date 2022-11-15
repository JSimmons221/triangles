import csv
from PIL import Image, ImageDraw
import os
import glob


#function to make a jpg of a triangle given 3 sets of coordinates and save it to a folder
def triangle(output_path, r):
    image = Image.new("RGB", (224, 224), "white")
    draw = ImageDraw.Draw(image)
    draw.polygon(((int(r[0]) + 12, int(r[1]) + 62), (int(r[2]), int(r[3]) + 62), (int(r[4]), int(r[5]) + 62)), outline="black")
    draw.polygon(((int(r[6]) + 124, int(r[7]) + 62), (int(r[8]) + 124, int(r[9]) + 62), (int(r[10]) + 124, int(r[11]) + 62)), outline="black")
    draw.line(((112, 0), (112, 224)), fill='black')
    image.save(output_path)


#clears all images from the images folder, used to keep things tidy
def clear_images():
    path = r'resources/images/*.jpg'
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
                triangle(r'resources/images/pair%i.jpg' % c, row)
            c += 1


csv_to_images(r'resources/triangles.csv')
