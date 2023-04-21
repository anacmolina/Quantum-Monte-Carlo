import setuptools

long_description = """
Python package for running Quantum Monte Carlo simulations
"""

setuptools.setup(
    name="quantum_monte_carlo",
    version="0.0.1",
    author="Ana Molina Taborda",
    author_email="anac.molina@udea.edu.co",
    description="Python package for running Quantum Monte Carlo simulations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
