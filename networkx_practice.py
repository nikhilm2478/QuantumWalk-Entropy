import networkx as nx
import matplotlib.pyplot as plt
import os
SHOTS = 4096

# inputted as a parameter
counts = {'00': 4096}

binToInt = lambda x: int(x, 2)
pos = {0: (-1, 1),  1: (-1,-1),  2: ( 1,-1),  3: ( 1, 1)}
nodeLabels = {0: '00', 1: '01', 2: '10', 3: '11'}
probs = {binToInt(node): counts.get(node, 0) / SHOTS for node in nodeLabels.values()}
blueMap = plt.colormaps['Blues']
nodeColors = [blueMap(value) for value in probs.values()]

graph = nx.DiGraph(nx.cycle_graph(4))

plt.clf()
plt.axis('equal')

nx.draw(graph, pos, labels=nodeLabels, node_size=1000, node_color=nodeColors, edge_color=['red', 'blue', 'green', 'black'], connectionstyle='arc3, rad=0.1')
nx.draw_networkx_edge_labels(graph, pos, label_pos=0.2)
sm = plt.cm.ScalarMappable(cmap=blueMap, norm=plt.Normalize(vmin=0, vmax=1))
plt.colorbar(sm, label='probability', ax=plt.gca())

plt.savefig('graph.png')
os.system('code graph.png')