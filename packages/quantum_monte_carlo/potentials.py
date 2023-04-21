### Potentials available for use in the Quantum Monte Carlo code

import numpy as np

### Define the harmonic oscillator potential
def harmonic_oscillator(x):
    """Harmonic oscillator potential
    
    Args:
        x (float): position of the particle
    Returns:
        float: value of the potential at x"""
    return 0.5*x**2