import qiskit as qk
import networkx as nx
import matplotlib.pyplot as plt
import os
backend = qk.Aer.get_backend('qasm_simulator')
TIME_STEPS = 10

os.system('cls' if os.name=='nt' else 'clear')

def runQuantumWalk(totalTime):
    # Quantum circuit setup
    c = qk.QuantumRegister(1, 'c')  # control bit
    v = qk.QuantumRegister(2, 'v')  # vertex bits
    m = qk.ClassicalRegister(2, 'm')  # measurement bits
    qc = qk.QuantumCircuit(c, v, m)

    # # Hadamard Gates
    # qc.h(v)

    # Setup qunatum walk
    for i in range(totalTime):
        qc.h(c)

        qc.ccx(c,v[0], v[1])
        qc.cx(c, v[0])
        qc.ccx(c,v[0], v[1], ctrl_state=0)
        qc.cx(c, v[0], ctrl_state=0)

    qc.measure(v, m)

    # Run simulation
    job = qk.execute(qc, backend)
    result = job.result()
    counts = result.get_counts()
    return dict(sorted(counts.items()))

def drawGraph(counts):
    pos = {0: (-1, 1),  1: (-1,-1),  2: ( 1,-1),  3: ( 1, 1)}
    nodeLabels = {i: f"{i:02b}" for i in range(4)}
    probs = {nodeInt: counts.get(node, 0)/1024 for nodeInt, node in nodeLabels.items()}
    blueMap = plt.colormaps['Blues']
    nodeColors = [blueMap(value) for value in probs.values()]

    graph = nx.DiGraph(nx.cycle_graph(4))

    plt.clf()
    plt.axis('equal')

    nx.draw(graph, pos, labels=nodeLabels, node_size=1000, node_color=nodeColors)
    sm = plt.cm.ScalarMappable(cmap=blueMap, norm=plt.Normalize(vmin=0, vmax=1))
    plt.colorbar(sm, label='probability', ax=plt.gca())

    plt.savefig('graph.png')
    os.system('code graph.png')

    return probs

# main
for i in range(0, TIME_STEPS+1):
    counts = runQuantumWalk(i)
    probs = drawGraph(counts)
    print(i, probs)