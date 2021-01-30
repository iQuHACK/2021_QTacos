from qiskit import execute

def measuring(circuit, backend, shots=2000):
    job = execute(circuit, backend, shots=shots)
    result = job.result()
    counts = result.get_counts()
    return {"|"+key+"⟩": f"{value*100/shots}%" for key, value in counts.items()}

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
        circuit.cx(channel, channel_op)
        
    return circuit