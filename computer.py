import perceval as pcvl
import perceval.lib.phys as phys
import sympy as sp


circuit = phys.Circuit(2)
circuit.add((0, 1), phys.BS(theta=sp.pi/4, phi_b=0))


simulator_backend = pcvl.BackendFactory().get_backend("Naive")
simulator = simulator_backend(circuit.U)

ca = pcvl.CircuitAnalyser(simulator,[pcvl.BasicState([0, 1]), pcvl.BasicState([1, 0])])

pcvl.pdisplay(ca)