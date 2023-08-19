import qiskit as qk
from qiskit import Aer
from qiskit.visualization import plot_histogram
from qiskit.visualization import circuit_drawer
import matplotlib.pyplot as plt
import os

# Quantum circuit setup
qc = qk.QuantumCircuit(2)
qc.h(0)
qc.h(1)

# qc.measure_all()

circuit_drawer(qc, output="mpl", filename="quantum_circuit.png")
os.system('code quantum_circuit.png')

# ---
input("Press enter to contine...")
# ---

#Run simulation
result = qk.execute(qc, Aer.get_backend('qasm_simulator')).result()
counts = result.get_counts(qc)
plot_histogram(counts)
plt.savefig('output.png')

print(counts)
os.system('code output.png')