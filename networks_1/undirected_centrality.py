import networkx as nx
import numpy as np
import random as r
from functools import reduce

def make_symmetric(matrix):
    size = matrix.shape[1]
    arr = np.array(matrix)
    for i in range(size):
        for k in range(size-i):
            j = size - k - 1
            arr[j][i] = arr[i][j]
    return np.matrix(arr)

def gen_graph(size, fill_prob=0.5):
    m = np.zeros((size, size))
    for i in range(size):
        for j in range(size - i - 1):
            m[i, i + j + 1] = 1 if r.random() < fill_prob else 0

    m = make_symmetric(m)
    return m

def s_dev(sample):
    mean = reduce(lambda y, x : y + x, sample)/len(sample)
    var = reduce(lambda y, x: y + (x - mean) ** 2, sample)/len(sample)
    return var ** 0.5

#code from https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Covariance
def covar(data_x, data_y):
    n = len(data_x)
    if n < 2:
        return 0
    kx = data_x[0]
    ky = data_y[0]
    Ex = Ey = Exy = 0
    for ix, iy in zip(data_x, data_y):
        Ex += ix - kx
        Ey += iy - ky
        Exy += (ix - kx) * (iy - ky)
    return (Exy - Ex * Ey / n) / n

def do_each_pair(data, names, function):
    s = set([i for i in range(len(data))])
    s2 = s.copy()
    d = []
    n = []
    for i in s:
        s2.remove(i)
        for j in s2:
            d.append(function(data[i], data[j]))
            n.append("{}-{}".format(names[i], names[j]))
    return (n, d)

def unpack_dict(d): #I'm surprised this works 
    return list(map(lambda x: d[x], list(d)))

def pearson(s1, s2):
    c = covar(s1, s2)
    if(c == 0):
        return 1
    return c/(s_dev(s1) * s_dev(s2))

reps = 50
samp_count = 40 #not including zero as a sample

samples = [i/samp_count for i in range(samp_count + 1)]

graph_size = 20

centrality_labels = ["deg", "close", "betw", "katz"]
count = len(centrality_labels)

data = []
names = []

name_count = round(count * (count - 1)/2)

for i in range(samp_count + 1):
    values = [0] * name_count
    data.append([])
    
    print("done {}/{}".format(i, samp_count))

    for re in range(reps):
        g = gen_graph(graph_size, samples[i])
        gn = nx.from_numpy_matrix(g)
        deg = unpack_dict(nx.degree_centrality(gn))
        clo = unpack_dict(nx.closeness_centrality(gn))
        bet = unpack_dict(nx.betweenness_centrality(gn))
        katz = unpack_dict(nx.katz_centrality(gn, 0.01))
        cents = []
        cents.append(deg)
        cents.append(clo)
        cents.append(bet)
        cents.append(katz)

        names, v = do_each_pair(cents, centrality_labels, pearson)


        for j in range(len(values)):
            values[j] += v[j]/reps
        
    for j in range(len(values)):
        data[i].append(values[j])

header = "density, {}".format(", ".join(str(x) for x in names))

f = open("undirected_centrality.csv", "w")
f.write(header)

for i in range(len(data)):
    data_str = "\n{}, {}".format(
            samples[i],
            ", ".join(str(x) for x in data[i]))
    f.write(data_str)

f.close()
