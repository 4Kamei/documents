import networkx as nx
import matplotlib.pyplot as plt

g = nx.read_gml("power.gml", label="id")

seed = 12313

options = {"node_size": 10, "node_color":"r"}
nx.draw(g, nx.spring_layout(g, seed=seed), **options)
plt.show()
