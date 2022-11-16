import math
import random as rand
import csv
import make_images as mi
import neural_network as nn

#Creates data for n pairs of triangles and puts them into the data set
def make_data(n, path):
    #sets the seed for rand
    rand.seed()
    #open the csv
    with open(path, 'w+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        #write the labels for the columns
        writer.writerow(['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'Congruent'])
        #make data and add to csv
        for i in range(n):
            print(i)
            writer.writerow(make_triangles())


#generates 3 points to act as the verticies of the triangle
def random_triangle():
    #return array
    ret = []

    #creating the first coordinate
    A = [rand.randint(5, 95), rand.randint(5, 95)]
    ret.append(A)

    #creating the second coordinate
    B = [rand.randint(5, 95), rand.randint(5, 95)]

    #while A and B are the same remake B
    while A == B:
        B = [rand.randint(5, 95), rand.randint(5, 95)]
    ret.append(B)

    #creating the third coordinate
    C = [rand.randint(5, 95), rand.randint(5, 95)]

    #while C is the same as A or B recreate it (note: idek the odds of this happening but w/e, can never be to safe)
    while C == A or C == B:
        C = [rand.randint(5, 95), rand.randint(5, 95)]
    ret.append(C)

    return ret


#Helper function for get_lens that returns the length from one vertex to another
def get_len(v1, v2):
    return (v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2


#returns the lengths of the three sides of a triangle and returns them as an array, sorted for easier comparison
def get_lens(t):
    lens = [get_len(t[0], t[1]), get_len(t[0], t[2]), get_len(t[1], t[2])]
    lens.sort()
    return lens


def transpose_triangle(t):
    t2 = t.copy()
    max_x = 100 - max(t[0][0], t[1][0], t[2][0])
    min_x = -1 * min(t[0][0], t[1][0], t[2][0])
    max_y = 100 - max(t[0][1], t[1][1], t[2][1])
    min_y = -1 * min(t[0][1], t[1][1], t[2][1])
    trans_x = min(95, max(5, rand.randint(min_x, max_x)))
    trans_y = min(95, max(5, rand.randint(min_y, max_y)))
    t[0][0] = t[0][0] + trans_x
    t[1][0] = t[1][0] + trans_x
    t[2][0] = t[2][0] + trans_x
    t[0][1] = t[0][1] + trans_y
    t[1][1] = t[1][1] + trans_y
    t[2][1] = t[2][1] + trans_y
    return t2


def check_valid(t):
    for coord in t:
        for j in coord:
            if not 5 < j < 95:
                return False
    return True


def rotate_coord(c, rad):
    x = c[0] - 50
    y = c[1] - 50
    cos = math.cos(rad)
    sin = math.sin(rad)
    x1 = int(x*cos - y*sin) + 50
    x2 = int(x*sin + y*cos) + 50
    return [x1, x2]


def rotate_triangle(t):
    angle = rand.randint(1, 359)
    rad = math.radians(angle)
    t2 = []
    for i in t:
        t2.append(rotate_coord(i, rad))

    c = 0
    while not check_valid(t2) and c < 100:
        t2.clear()
        angle = rand.randint(1, 359)
        rad = math.radians(angle)
        for i in t:
            t2.append(rotate_coord(i, rad))
        c += 1

    if c >= 100:
        t2 = t.copy()

    return t2


#helps to create the second triangle for the dataset
def second_triangle(t1):
    #generate a new triangle
    t2 = random_triangle()

    #while they have the same side lengths (congruent) remake t2 (note: odds are even less on this one but once again, w/e)
    while get_lens(t1) == get_lens(t2):
        t2 = random_triangle()

    return t2


#creates the two triangles
def make_triangles():

    #create the first triangle
    t1 = random_triangle()
    ret = []

    #ret needs to be an array of just ints but it's easier to think of triangles as 3 coordinates rather than 6 ints so this happens
    for i in t1:
        for j in i:
            ret.append(j)

    #if r is 1, the triangles are the same (copy t1 into ret again) and add 1 to signify they are the same
    if rand.randint(0, 1):
        r = rand.randint(0,3)
        t2 = t1.copy()

        if r == 1:
            t2 = rotate_triangle(t2)
        elif r == 2:
            t2 = transpose_triangle(t2)
        elif r == 3:
            t2 = rotate_triangle(t2)
            t2 = transpose_triangle(t2)

        for i in t2:
            for j in i:
                ret.append(j)
        ret.append(1)

    # if r is 0, the two triangles are different (create a new triangle t2 and add to ret) add 0 to signify they are different
    else:
        t2 = second_triangle(t1)
        if rand.randint(0, 1):
            t2 = transpose_triangle(t2)
        for i in t2:
            for j in i:
                ret.append(j)
        ret.append(0)

    return ret


make_data(3000, r'Resources/triangles.csv')
print("made triangles")
mi.csv_to_images(r'Resources/triangles.csv')
print("made images")
data, target = nn.load_my_fancy_dataset()
print("created dataset")
nn.train(data, target)
print("done")

