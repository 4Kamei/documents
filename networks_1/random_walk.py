import random as r
from functools import reduce
import numpy as np

def iterate(sample):
    for i in range(len(sample)):
        sample[i] += -1 if r.random() < 0.5 else 1
    return sample

def get_data(sample):
    (vals, freq) = np.unique(sample, return_counts=True)

#start with 100 values
sample = [0 for i in range(100)]

