import numpy as np
import matplotlib.pyplot as plt
from epidemic.sir_model import SIRModel
from epidemic.visualize import plot_sir_model

# Parameters
beta = 10  # Transmission rate
sigma = 1  # Recovery rate
initial_infected = 10
population = 1000
days = 5
num_simulations =1000 # Number of simulations to generate
dt =0.01 # Time Step

# Lists to store final infected counts for each simulation
final_infected_counts = []

# Run multiple simulations
for _ in range(num_simulations):
    # Create and simulate the SIR model
    model = SIRModel(beta, sigma, initial_infected, population)
    #Simulate the model for specific numver of days with a time step 
    
    model.simulate(days,dt)
    # Store the final infected count from each simulation
    final_infected_counts.append(model.I[-1])

# Visualize the results
#plot_sir_model(model)

# Create a histogram of the final infected counts
plt.figure(figsize=(10, 6))
plt.hist(final_infected_counts, bins=20, edgecolor='black')
plt.xlabel('Final Infected Count')
plt.ylabel('Frequency')
plt.title(f'Distribution of Final Infected Counts (Simulations: {num_simulations})')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
