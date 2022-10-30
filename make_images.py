import csv
from PIL import Image, ImageDraw
import os
import glob


#function to make a jpg of a triangle given 3 sets of coordinates and save it to a folder
def triangle(output_path, r):
    image = Image.new("RGB", (700, 300), "white")
    draw = ImageDraw.Draw(image)
    draw.polygon(((int(r[0]), int(r[1])), (int(r[2]), int(r[3])), (int(r[4]), int(r[5]))), outline="black")
    draw.polygon(((int(r[6]) + 400, int(r[7])), (int(r[8]) + 400, int(r[9])), (int(r[10]) + 400, int(r[11]))), outline="black")
    draw.line(((350, 0), (350, 300)), fill='black')
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
