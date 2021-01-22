import networkx as nx
import numpy as np
from functools import reduce
import matplotlib.pyplot as plt

adj_matrix = np.matrix("""
        0 1 1 0 1 0 0 0 0 0;
        1 0 1 0 1 0 1 0 0 1;
        1 1 0 1 1 1 0 0 0 0;
        0 0 1 0 0 1 0 0 0 0;
        1 1 1 0 0 1 1 0 0 0;
        0 0 1 1 1 0 1 1 0 0;
        0 1 0 0 1 1 0 1 0 0;
        0 0 0 0 0 1 1 0 1 0;
        0 0 0 0 0 0 0 1 0 1;
        0 1 0 0 0 0 0 0 1 0
        """)

print("Is symmetric? {}".format((np.transpose(adj_matrix) == adj_matrix).all()))

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

cl = []
for i in range(10):
    cl.append(clustering(adj_matrix, i))

g_cl = reduce(lambda y, x: y + x, cl)/10

print(cl)

print(g_cl)

cl_str = list(map(lambda x : round(x, 2), cl))

labels = dict(enumerate(cl_str))

print(labels)

g = nx.from_numpy_matrix(adj_matrix)
layout = nx.spring_layout(g, seed = 12334)

nx.draw(g, layout, node_color="lightblue", node_size=400)
nx.draw_networkx_labels(g, layout, labels, )

plt.show()
