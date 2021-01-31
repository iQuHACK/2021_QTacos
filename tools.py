import numpy as np
from qiskit import execute
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