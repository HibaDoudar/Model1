import argparse
from epidemic.sir_model import SIRModel

def run_sir_model_cli():
    parser = argparse.ArgumentParser(description='SIR Model Simulator')
    parser.add_argument('--beta', type=float, default=10, help='Transmission rate')
    parser.add_argument('--sigma', type=float, default=1, help='Recovery rate')
    parser.add_argument('--initial_infected', type=int, default=10, help='Initial infected individuals')
    parser.add_argument('--population', type=int, default=1000, help='Total population')
    parser.add_argument('--days', type=int, default=5, help='Number of simulation days')
    parser.add_argument('--dt', type=float, default=0.01, help='Number of time step')
    
    args = parser.parse_args()
    
    model = SIRModel(args.beta, args.sigma, args.initial_infected, args.population)
    model.simulate(args.days, args.dt)
    model.step( args.dt)
    
    # Print or save the results as needed

if __name__ == '__main__':
    run_sir_model_cli()
