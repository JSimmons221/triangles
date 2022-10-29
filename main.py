import random
import random as rand
import csv


#Creates data for n pairs of triangles and puts them into the data set
def make_data(n, path):
    rand.seed()
    #open the csv
    with open(path, 'w+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        #write the labels for the columns
        writer.writerow(['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'Congruent'])
        #make data and add to csv
        for i in range(n):
            writer.writerow(make_triangles())


#generates 3 points to act as the verticies of the triangle
def random_triangle():
    ret = []
    A = [rand.randint(25, 275), rand.randint(25, 275)]
    ret.append(A)

    B = [rand.randint(25, 275), rand.randint(25, 275)]
    while A == B:
        B = [rand.randint(25, 275), rand.randint(25, 275)]
    ret.append(B)

    C = [rand.randint(25, 275), rand.randint(25, 275)]
    while C == A or C == B:
        C = [rand.randint(25, 275), rand.randint(25, 275)]
    ret.append(C)

    return ret


def get_len(a1, a2):
    return (a1[0] - a2[0]) ** 2 + (a1[1] - a2[1]) ** 2


def get_lens(t):
    lens = [get_len(t[0], t[1]), get_len(t[0], t[2]), get_len(t[1], t[2])]
    lens.sort()
    return lens


#helps to create the second triangle for the dataset
def second_triangle(t1):
    t2 = random_triangle()

    while get_lens(t1) == get_lens(t2):
        t2 = random_triangle()

    return t2

def make_triangles():
    r = random.randint(0, 1)
    t = random_triangle()
    ret = []

    for i in t:
        for j in i:
            ret.append(j)

    if r == 0:
        for i in t:
            for j in i:
                ret.append(j)
        ret.append(0)

    elif r == 1:
        t2 = second_triangle(t)
        for i in t2:
            for j in i:
                ret.append(j)
        ret.append(1)

    return ret


make_data(50, r'resources/triangles.csv')
