import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

seed = 123109283

g = nx.read_gml("lesmis.gml")

nodes = g.degree
nodes = sorted(nodes, key=lambda x : x[1], reverse=True)

(largest, degree) = nodes[0]

ego = nx.ego_graph(g, largest)
pos = nx.spring_layout(ego, seed=seed)
nx.draw(ego, pos, node_color="lightblue", node_size = 50, with_labels=True)

options = {"node_size": 300, "node_color":"r"}
nx.draw_networkx_nodes(ego, pos, nodelist=[largest], **options)
#plt.show()

degrees = list(map(lambda x : x[1], nodes))


(vals, freq) = np.unique(degrees, return_counts=True)

print(vals)
print(freq)

plt.clf()

plt.bar(vals, freq)
plt.xlabel("Node Degree")
plt.ylabel("Degree Frequency")
plt.title("Les Miserables degree distribution for characters appearing in same chapter")
plt.show()
