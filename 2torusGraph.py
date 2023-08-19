import networkx as nx
import matplotlib.pyplot as plt
import os
import numpy as np
np.set_printoptions(threshold=np.inf, linewidth=np.inf, precision=2)

def showGraph(G):
    pos = nx.spring_layout(G, seed=42)  # Adjust layout for better visualization
    nx.draw(G, pos, with_labels=True)
    plt.savefig('output.png')
    os.system('code output.png')

def cls():
    os.system('cls')

cls()

# Create a 4x3 torus grid graph
G = nx.grid_2d_graph(4, 3, periodic=True)

showGraph(G)

print("Original adjacency matrix")
A = nx.to_numpy_array(G)
print(A)

print("Original Transition matrix")
M = A / A.sum(axis=0)
print(M)

# Initialize the probability vector at node (0, 0)
prob_vector = np.zeros(G.number_of_nodes())
prob_vector[0] = 1.0

for i in range(2, 514):
    cls()
    print("Power", i)
    print()
    print("Adjacency matrix")
    print(np.linalg.matrix_power(A, i))
    print()
    print("Transition matrix")
    print(np.linalg.matrix_power(M, i))

    # Update the probability vector using the transition matrix
    prob_vector = np.dot(prob_vector, M)

    print()
    print("Probability vector")
    print(prob_vector)