import csv
from PIL import Image, ImageDraw


def triangle(output_path, a1, a2, b1, b2, c1, c2):
    image = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(image)
    draw.polygon(((a1, a2), (b1, b2), (c1, c2)), outline="black")

    image.save(output_path)


def csv_to_images(path):
    with open(path) as file:
        reader = csv.reader(file, delimiter=',')
        c = 0
        for row in reader:
            if c != 0:
                triangle(r'resources/images/pair%i_1.jpg' % c, int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]))
                triangle(r'resources/images/pair%i_2.jpg' % c, int(row[6]), int(row[7]), int(row[8]), int(row[9]), int(row[10]), int(row[11]))
            c += 1


csv_to_images(r'resources/triangles.csv')
