import random as r
from functools import reduce

r.seed(123879023457)

def sample(prob, counts):
    out = []
    for i in range(counts):
        out.append(1 if prob > r.random() else 0)
    return out

def moment(order, sample):
    size = len(sample)
    m = reduce(lambda x, y: x + y ** order, sample)
    return m/size

def var(sample):
    return moment(2, sample) - moment(1, sample) ** 2

#generate 100 values of p
p = [i/100 for i in range(101)]
out = []
for i in range(len(p)):
    s = sample(p[i], 1000)
    out.append(var(s))

f = open("bernoulli_out.csv", "w")
f.write("p, var")

for i in range(len(p)):
    f.write("\n{}, {}".format(p[i], out[i]))

f.close()
