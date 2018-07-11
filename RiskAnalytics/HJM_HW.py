from numpy import exp, sqrt
from numpy.random import normal


class HW:
    
    def __init__(self,sigma, kappa, dt, Libor_rates, Swap_rates, maturity):
        self.sigma = sigma #   sigma: constant volatility parameter
        self.kappa = kappa#   kappa: volatility mean reversion
        self.dt = dt#   dt: time step
        self.forward_rate = Swap_rates
        self.Libor_rates = Libor_rates#   Libor_rates: for maturities less than one year
        self.Swap_rates = Swap_rates#   Swap_rates: for maturities greater than one year
        self.maturity = maturity#   maturity: in years

    def buildForwardCurve(self,Libor_rates, Swap_rates):
        self.forward_rate = Swap_rates
        return self.forward_rate

    def simulateShortRate(self):
        for t in range(1, self.maturity/self.dt):
            r(t + 1)=r(t)+self.forward_rate(t+1)-self.forward_rate(t)
            r(t + 1) += (self.sigma ^ 2 * (1 - exp(-2 * self.kappa * (t + 1))) / (2 * self.kappa)) * self.dt
            r(t + 1) += self.kappa * self.dt * (self.forward_rate(t)- r(t))
            r(t + 1) += self.sigma * sqrt(self.dt) * normal(0,1,1)
        return r
