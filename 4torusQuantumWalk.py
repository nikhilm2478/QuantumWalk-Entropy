import qiskit as qk
from qiskit.circuit.library.standard_gates.x import XGate
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import os
backend = qk.Aer.get_backend("qasm_simulator")

os.system("cls" if os.name == "nt" else "clear")
def printProbs(dictionary, rows=4, cols=4):
    for y in range(rows - 1, -1, -1):
        for x in range(cols):
            key = f'{x:02b} {y:02b}'
            value = dictionary.get(key, 0)
            rounded_value = round(value, 3)
            print(f'({x},{y}): {rounded_value}', end='\t')
        print()

def runQuantumWalk(totalTime: int):
    # Quantum circuit setup
    c = qk.QuantumRegister(2, "c")  # control bits
    x = qk.QuantumRegister(2, "x")  # x bits
    y = qk.QuantumRegister(2, "y")  # y bits
    mX = qk.ClassicalRegister(2, "mX")  # measurement bits for x
    mY = qk.ClassicalRegister(2, "mY")  # measurement bits for y
    qc = qk.QuantumCircuit(c, x, y, mY, mX)

    # # Hadamard Gates
    # qc.h(x)
    # qc.h(y)

    # Setup qunatum walk
    for i in range(totalTime):
        qc.h(c)
        
        qc.append(XGate().control(3, ctrl_state="000"), [c[0],c[1],x[0], x[1]])
        qc.append(XGate().control(2, ctrl_state= "00"), [c[0],c[1],      x[0]])
        qc.append(XGate().control(3, ctrl_state="110"), [c[0],c[1],x[0], x[1]])
        qc.append(XGate().control(2, ctrl_state= "10"), [c[0],c[1],      x[0]])

        qc.append(XGate().control(3, ctrl_state="001"), [c[0],c[1],y[0], y[1]])
        qc.append(XGate().control(2, ctrl_state= "01"), [c[0],c[1],      y[0]])
        qc.append(XGate().control(3, ctrl_state="111"), [c[0],c[1],y[0], y[1]])
        qc.append(XGate().control(2, ctrl_state= "11"), [c[0],c[1],      y[0]])
    
    qc.measure(x, mX)
    qc.measure(y, mY)
    
    # Run simulation
    job = qk.execute(qc, backend, shots=4096)
    result = job.result()
    counts = result.get_counts()
    return dict(sorted(counts.items()))

def drawGraph(counts: dict[str, int], curTime: int):
    nodeLabels = {(i,j): f"{i:02b} {j:02b}" for i in range(4) for j in range(4)}
    probs = {node: counts.get(node, 0)/4096 for node in nodeLabels.values()}
    print("\ntime =",i); printProbs(probs)

    blueMap = colors.LinearSegmentedColormap.from_list('GradientCmap', list(zip([0.0, 0.5, 1.0], ['#FFFFFF', '#0000FF', '#000000'])))
    nodeColors = [blueMap(value) for value in probs.values()]
    pos = {(i,j): (i,j) for i in range(4) for j in range(4)}
    graph = nx.grid_2d_graph(4,4, periodic=True, create_using=nx.DiGraph)

    plt.clf()
    plt.axis('equal')
    plt.title(f'time = {curTime}')

    nx.draw(graph, pos, labels=nodeLabels, node_size=1500, node_color=nodeColors)
    sm = plt.cm.ScalarMappable(cmap=blueMap, norm=plt.Normalize(vmin=0, vmax=1))
    plt.colorbar(sm, label='probability', ax=plt.gca())

    plt.savefig('graph.png')
    os.system('code graph.png')

def drawHistogram(counts):
    nodeLabels = {(i,j): f"{i:02b} {j:02b}" for i in range(4) for j in range(4)}
    probs = {node: counts.get(node, 0)/4096 for nodeInt, node in nodeLabels.items()}

    plt.clf()
    plt.ylim(0, 1)
    plt.bar(probs.keys(), probs.values())
    plt.savefig('histogram.png')
    os.system('code histogram.png')

# main
for i in range(0, 10):
    counts = runQuantumWalk(i)

    drawGraph(counts, i)
    # drawHistogram(counts)