import numpy as np
import random
from qiskit import QuantumCircuit, Aer, execute
from scipy.spatial.distance import cosine


def measuring(circuit, backend, shots=2000):
    job = execute(circuit, backend, shots=shots)
    result = job.result()
    counts = result.get_counts()
    return {key: value*100.0/shots for key, value in counts.items()}

def add_gate(circuit, gate=None, channel=0, channel_op=0):
    if gate == "hadamard":
        circuit.h(channel)
    
    elif gate == "x":
        circuit.x(channel)
    
    elif gate == "y":
        circuit.y(channel)
    
    elif gate == "z":
        circuit.z(channel)
    
    elif gate == "cnot":
        circuit.cnot(channel, channel_op)
        
    return circuit

def randomQuantumState():
    qc = QuantumCircuit(3,3)
    for i in range(0,int(random.randint(1,5))):
        g = random.choice(("hadamard","x","y","z","cnot"))
        if g == "cnot":
            q = random.sample(tuple(range(0,3)),2)
            add_gate(qc,gate=g,channel=q[0],channel_op=q[1])
        else:
            q = random.choice(tuple(range(0,3)))
            add_gate(qc,gate=g,channel=q)

    qc.barrier()
    qc.measure([0,1,2],[0,1,2])
    qc.draw('mpl')
    
    simulator = Aer.get_backend('qasm_simulator')
    rqs = measuring(qc, backend=simulator)
    return rqs

def dictovec(dic):
    base_states = [f"{a}"+f"{b}"+f"{c}" for a in range(2) for b in range(2) for c in range(2)]
    
    for base in base_states:
        if base in dic.keys():
            continue
        else:
            dic[base] = 0.0
        
    return np.array([dic[base] for base in base_states])


def similarity(dic1, dic2, err=0.01):
    v1 = dictovec(dic1)
    v2 = dictovec(dic2)
    distance = cosine(v1, v2)
    
    if distance <= err:
        return True, distance
    else:
        return False, distance
