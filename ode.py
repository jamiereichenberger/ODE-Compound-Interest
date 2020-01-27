#Project 1 - Visualize ODE with SciPy 
#Team 6 - Jamie (Graham) Reichenberger, Tristan Janisse. Natsuki Abe 
#Professor Ricardo Citro – CST305 - MWF 3:20-4:30  
#January 26, 2020 

#Initalizing the libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#Creates the equation that will be differentiated
def CompoundInterest(S,t):
    dSdt = r*S
    return dSdt

#Initial amount of money as entered by the user
S0 = int(input("Enter the amount of money: "))

#Sets the amount of time money will be compounded for
t = np.linspace(0,20)
#Sets what rate the money will compound each year
r = float(input("Enter the rate of return(decimal): "))

#Differentiates the equation
S = odeint(CompoundInterest, S0, t)
#Plots all the time and money points
plt.plot(t,S)
plt.xlabel('Year')
plt.ylabel('Dollars')
plt.show()
