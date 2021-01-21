import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#read in, with the label being the "id" attribute
g = nx.read_gml("power.gml", label="id")

#map to array of degree for each node
nodes = list(map(lambda x : x[1], g.degree))

#extract frequency information 
(val, freq) = np.unique(nodes, return_counts=True)

#write out the degree distribution to analyize in R 

f = open("power_dist.csv", "w")
f.write("degree, frequency")
for i in range(len(val)):
    f.write("\n{}, {}".format(val[i], freq[i]))
    

