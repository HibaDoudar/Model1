import numpy as np

class SIRModel:
    def __init__(self, beta, sigma, initial_infected, population):
        self.beta = beta  #  Transmission rate (probability of transimision per contact)
        self.sigma = sigma  # Recovery rate (probability of recovery per unit of time)
        self.S = [population - initial_infected]  # Susceptible
        self.I = [initial_infected]  # Iinital number of infectious individuals
        self.R = [0]  # Recovered
        

    def step(self, dt):
            S_last = self.S[-1]
            I_last = self.I[-1]
            R_last =self.R[-1]
            #calculate the number of new infections using binomial distribution
            new_infections = np.random.binomial(S_last, 1- np.exp(-self.beta * I_last/(S_last+I_last+R_last)*dt),1)[0]
            
            dS= - new_infections * dt
            dI= (new_infections - self.sigma*I_last)*dt
            dR = (self.sigma * I_last)*dt

            #update compartment counts
           
            S_new= S_last +dS
            I_new = I_last +dI
            R_new = R_last+dR
            self.S.append(S_new)
            self.I.append(I_new)
            self.R.append(R_new)


    def simulate(self,days, dt):
        for _ in range(int(days/dt)):
            self.step(dt)
