import numpy as np
import matplotlib.pyplot as plt
from epidemic.sir_model import SIRModel

# Parameters
beta = 1  # Transmission rate
sigma = 10  # Recovery rate
initial_infected = 10
population = 1000
days = 5
num_simulations = 1000  # Number of simulations to generate a distribution
dt = 0.01  # Time step

# Lists to store final infected counts for each simulation
final_infected_counts = []

# Run multiple simulations
for _ in range(num_simulations):
    # Create and simulate the SIR model with time step
    model = SIRModel(beta, sigma, initial_infected, population)
    for day in np.arange(0, days, dt):
        model.step(dt)
    
    # Store the final infected count from each simulation
    final_infected_counts.append(model.I[-1])

# Create a histogram of the final infected counts
plt.figure(figsize=(10, 6))
plt.hist(final_infected_counts, bins=20, edgecolor='black')
plt.xlabel('Final Infected Count')
plt.ylabel('Frequency')
plt.title(f'Distribution of Final Infected Counts (Simulations: {num_simulations})')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
