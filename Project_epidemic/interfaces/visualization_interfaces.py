import matplotlib.pyplot as plt
from epidemic.sir_model import SIRModel

def visualize_sir_model(model):
    plt.figure(figsize=(10, 6))
    plt.plot(model.S, label='Susceptible')
    plt.plot(model.I, label='Infectious')
    plt.plot(model.R, label='Recovered')
    plt.xlabel('Days')
    plt.ylabel('Number of Individuals')
    plt.legend()
    plt.title('SIR Model')
    plt.show()

# Example usage:
model = SIRModel(10, 1, 10, 1000, 0.01)
model.simulate(100,0.01)
visualize_sir_model(model)
