import matplotlib.pyplot as plt

def plot_sir_model(sir_model):
    plt.figure(figsize=(10, 6))
    plt.plot(sir_model.S, label='Susceptible')
    plt.plot(sir_model.I, label='Infectious')
    plt.plot(sir_model.R, label='Recovered')
    plt.xlabel('Days')
    plt.ylabel('Number of Individuals')
    plt.legend()
    plt.title('SIR Model')
    plt.show()
