import numpy as np

# Classic particle probability
def classical_particle_probability(x, V, T):
    """Classical particle probability.
    Args:
        x (float): position of the particle
        V (function): potential energy function
        T (float): temperature
    Returns:
        float: probability of the particle being at x"""
    beta = 1/T
    return np.exp(-beta*V(x))
        
