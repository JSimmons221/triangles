import math
import random as rand
import csv
import numpy as np


# new stuff
# ----------------------------------------------------------------------------------------------------------------------
# generates 3 points to act as the verticies of the triangle
def random_triangle():
    # return array
    ret = []

    # creating the first coordinate
    A = [rand.randint(5, 95), rand.randint(5, 95)]
    ret.append(A)

    # creating the second coordinate
    B = [rand.randint(5, 95), rand.randint(5, 95)]

    # while A and B are the same remake B
    while A == B:
        B = [rand.randint(5, 95), rand.randint(5, 95)]
    ret.append(B)

    # creating the third coordinate
    C = [rand.randint(5, 95), rand.randint(5, 95)]

    # while C is the same as A or B recreate it (note: idek the odds of this happening but w/e, can never be to safe)
    while C == A or C == B:
        C = [rand.randint(5, 95), rand.randint(5, 95)]
    ret.append(C)

    return ret


def random_rectangle():
    len1 = rand.randint(10, 90)
    if rand.randint(0, 1):
        len2 = len1
    else:
        len2 = rand.randint(10, 90)

    x1 = rand.randint(5, 95 - len1)
    y1 = rand.randint(5, 95 - len1)

    return [[x1, y1], [x1 + len1, y1], [x1 + len1, y1 + len2], [x1, y1 + len2]]


def transpose_shape(s):
    s2 = s.copy()
    x = []
    y = []
    for i in s2:
        x.append(i[0])
        y.append(i[1])

    max_x = 95 - np.amax(x)
    min_x = 5 - 1 * np.amin(x)
    max_y = 95 - np.amax(y)
    min_y = 5 - 1 * np.amin(y)

    trans_x = rand.randint(min_x, max_x)
    trans_y = rand.randint(min_y, max_y)

    for i in range(0, len(s2)):
        s2[i][0] = s2[i][0] + trans_x
        s2[i][1] = s2[i][1] + trans_y

    return s2


def rotate_coord(c, rad):
    x = c[0] - 50
    y = c[1] - 50
    cos = math.cos(rad)
    sin = math.sin(rad)
    x1 = int(x*cos - y*sin) + 50
    x2 = int(x*sin + y*cos) + 50
    return [x1, x2]


def check_valid(s):
    for coord in s:
        for i in coord:
            if not 5 < i < 95:
                return False
    return True


def rotate_shape(s):
    angle = rand.randint(1, 359)
    rad = math.radians(angle)
    s2 = []
    for i in s:
        s2.append(rotate_coord(i, rad))

    c = 0
    while not check_valid(s2) and c < 100:
        s2.clear()
        angle = rand.randint(1, 359)
        rad = math.radians(angle)
        for i in s:
            s2.append(rotate_coord(i, rad))
        c += 1

    if c >= 100:
        s2 = s.copy()

    return s2


# Helper function for get_lens that returns the length from one vertex to another
def get_len(v1, v2):
    return (v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2


# returns the lengths of the three sides of a triangle and returns them as an array, sorted for easier comparison
def get_lens(t):
    lens = [get_len(t[0], t[1]), get_len(t[0], t[2]), get_len(t[1], t[2])]
    lens.sort()
    return lens


# helps to create the second triangle for the dataset
def second_triangle(t1):
    # generate a new triangle
    t2 = random_triangle()

    # while they have the same side lengths (congruent) remake t2 (note: odds are even less on this one but once again, w/e)
    while get_lens(t1) == get_lens(t2):
        t2 = random_triangle()

    return t2


def make_shapes():
    # Can be increased if more shapes added, 0 = triangle, 1 = square
    shape = rand.randint(0,1)
    s1 = []
    if shape == 0:
        s1 = random_triangle()
    if shape == 1:
        s1 = rotate_shape(random_rectangle())

    ret = []

    # 1 = same shape, 2 =
    if rand.randint(0,1):
        ret = [s1, s1, 1]
    else:
        s2 = []
        # 1 = same type of shape, 2 = different shape
        if rand.randint(0,1):
            if shape == 0:
                s2 = random_triangle()
            if shape == 1:
                s2 = rotate_shape(random_rectangle())
            ret = [s1, s2, 2]

        else:
            if shape == 0:
                s2 = rotate_shape(random_rectangle())
            if shape == 1:
                s2 = random_triangle()
            ret = [s1, s2, 3]



    return ret


def make_data2(n, path):
    # sets the seed for rand
    rand.seed()
    # open the csv
    with open(path, 'w+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        # write the labels for the columns
        writer.writerow(['Polygon 1', 'Polygon 2', 'Congruent'])
        # make data and add to csv
        for i in range(n):
            writer.writerow(make_shapes())


# old stuff
# ----------------------------------------------------------------------------------------------------------------------
# Creates data for n pairs of triangles and puts them into the data set
def make_data(n, path):
    # sets the seed for rand
    rand.seed()
    # open the csv
    with open(path, 'w+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        # write the labels for the columns
        writer.writerow(['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'Congruent'])
        # make data and add to csv
        for i in range(n):
            print(i)
            writer.writerow(make_triangles())


# creates the two triangles
def make_triangles():

    # create the first triangle
    t1 = random_triangle()
    ret = []

    # ret needs to be an array of just ints but it's easier to think of triangles as 3 coordinates rather than 6 ints so
    # this happens
    for i in t1:
        for j in i:
            ret.append(j)

    # if r is 1, the triangles are the same (copy t1 into ret again) and add 1 to signify they are the same
    if rand.randint(0, 1):
        r = rand.randint(0,3)
        t2 = t1.copy()

        if r == 1:
            t2 = rotate_shape(t2)
        elif r == 2:
            t2 = transpose_shape(t2)
        elif r == 3:
            t2 = rotate_shape(t2)
            t2 = transpose_shape(t2)

        for i in t2:
            for j in i:
                ret.append(j)
        ret.append(1)

    # if r is 0, the two triangles are different (create a new triangle t2 and add to ret) add 0 to signify they are
    # different
    else:
        t2 = second_triangle(t1)
        for i in t2:
            for j in i:
                ret.append(j)
        ret.append(0)

    return ret


make_data2(20, r'resources/shapes.csv')
