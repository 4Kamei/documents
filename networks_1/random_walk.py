import random as r
from functools import reduce
import numpy as np

SAMPLE_COUNT = 10000

def iterate(sample):
    for i in range(len(sample)):
        sample[i] += -1 if r.random() < 0.5 else 1
    return sample

def get_data(sample):
    (vals, freq) = np.unique(sample, return_counts=True)
    freq = list(map(lambda x: x/SAMPLE_COUNT, freq))
    return (vals, freq)

#start with 1000 values
sample = [0 for i in range(SAMPLE_COUNT)]

max_iter = 1000

for i in range(max_iter):
    #iterate the random walk
    sample = iterate(sample)

#save the final sample

vals, freq = get_data(sample)

f = open("random_walk.csv", "w")
f.write("pos, prob")
for j in range(len(freq)):
    f.write("\n{}, {}".format(vals[j], freq[j]))
f.close()
