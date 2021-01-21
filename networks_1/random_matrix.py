import numpy as np
import random as r

def setup_matrix(size, prob):
    mat = np.zeros((size, size))
    for i in range(size):
        for k in range(size - i):
            j = size - k - 1
            mat[i][j] = 1 if r.random() < prob else 0 
            mat[j][i] = mat[i][j]
    return mat

eigs = []

size = 1000
reps = 10

print("generating")
for i in range(reps):
    if(i % round(reps/10) == 0):
        print("{}% done".format(i * 100 / reps))
    eigs.append(np.linalg.eigvalsh(setup_matrix(size, 0.5)))

hist = {}

keys = set()

print("analysing")

for i in range(reps):
    for j in range(size):
        v = round(eigs[i][j])
        if(v in keys):
            hist[v] += 1
        else:
            hist[v] = 1
            keys.add(v)

print(hist)

f = open("mat_eigs.csv", "w")
f.write("bin, freq")
for i in keys:
    f.write("\n{}, {}".format(i, hist[i]))

f.close()
