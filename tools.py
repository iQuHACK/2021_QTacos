from qiskit import QuantumCircuit, Aer, execute

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