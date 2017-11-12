from numpy import exp

class HW:

    def __init__(self,sigma, kappa, dt, Libor_rates, Swap_rates):
        self.sigma = sigma
        self.kappa = kappa
        self.dt = dt
        self.forward_rate = Swap_rates
        self.Libor_rates = Libor_rates
        self.Swap_rates = Swap_rates


    def buildForwardCurve(self,Libor_rates, Swap_rates):


    def simulateShortRate(self):
        r(t+1)=r(t)+forward_M(t+1)-forward_M(t+1)+(self.sigma^2*(1-exp(-2*self.kappa*(t+1)))/(2*self.kappa)+)

