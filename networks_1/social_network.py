import networkx as nx
import numpy as np
import random as r
import matplotlib.pyplot as plt
from functools import reduce

def degree(adj_matrix, nodeid):
    return reduce(lambda y, x: y + 1 if x > 0 else y, np.array(adj_matrix)[nodeid])

def clustering(adj_matrix, nodeid):
    #set of nodes connected to nodeid
    arr = np.array(adj_matrix)
    connected = set()
    max_id = len(arr[nodeid])
    for i in range(max_id):
        if(adj_matrix[nodeid, i] > 0):
            connected.add(i)
    con_copy = connected.copy()
    tri_num = 0
    for i in connected:
        con_copy.remove(i)
        for j in con_copy:
            tri_num += 1 if adj_matrix[i, j] > 0 else 0
    deg = degree(adj_matrix, nodeid)
    return 2 * tri_num/(deg*(deg - 1))

#randrange but supports empty
def rand(x):
    if(x == 0):
        return 0
    return r.randrange(x)

#copies the top triangle entries to the bottom triangle and returns
def make_symmetric(matrix):
    size = matrix.shape[1]
    arr = np.array(matrix)
    for i in range(size):
        for k in range(size-i):
            j = size - k - 1
            arr[j][i] = arr[i][j]
    return np.matrix(arr)

def gen_lattice_adj(max_sep, shortcuts, size, seed=None):
    print("doing {}, {}, {}".format(max_sep, shortcuts, size))
    if(not not seed):
        r.seed(seed)
    #firstly, generate a non-shortcut lattice
    matr = np.zeros((size, size))
    for node in range(size):
        for i in range(max_sep):
            k = (node + i + 1) % size
            a = min(node, k)
            b = max(node, k)
            matr[a, b] = 1
    
    matr = make_symmetric(matr)

    while(shortcuts > 0):
        #generates an x value for the position to place the shortcut, 
        #in the upper triangle bounded from below by ones
        randx = max_sep + 1 + rand(size - max_sep - 1) 
        randy = rand(randx)
        if(not matr[randy, randx]):
            matr[randy, randx] = 1
            shortcuts -= 1

    return make_symmetric(matr)

first = True


size = 20
k = 3
reps = 1

max_shorts = (size - k)*(size - k - 1)/2 - k*(k+1)/2

print(max_shorts)

shortcuts = [i for i in range(round(max_shorts + 1))]

shortcuts = [0, max_shorts]

diams = []
coeff = []

for short_num in shortcuts:
    d = 0
    c = 0
    for rep in range(reps):
        lattice = gen_lattice_adj(k, short_num, size)
        print(lattice)

        gr = nx.from_numpy_matrix(lattice)
        d += nx.diameter(gr)
        
        cl = []
        for i in range(size):
            cl.append(clustering(lattice, i))
        c += reduce(lambda y, x: y + x, cl)/size
    diams.append(d/reps)
    coeff.append(c/reps)

print(diams)
print(coeff)

f = open("social_data.csv", "w")
f.write("short, diam, cls")
for i in range(len(shortcuts)):
    f.write("\n{}, {}, {}".format(shortcuts[i], diams[i], coeff[i]))

f.close()

"""
print(lattice)

gr = nx.from_numpy_matrix(lattice)

layout = nx.circular_layout(gr, dim=2, scale=1)
nx.draw(gr, layout)

plt.show()
"""




