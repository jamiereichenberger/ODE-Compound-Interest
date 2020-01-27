# ODE-Compound-Interest
Project 1 - create ODE that generates simple compound interest
Team 6 - Jamie (Graham) Reichenberger, Tristan Janisse. Natsuki Abe 
Professor Ricardo Citro – CST305 - MWF 3:20-4:30  
January 26, 2020 

# Set up instructions:
## 1. Install Python 2.7 on computer

## 2. Download Github code into your computer as a python file

## 3. Run the command "python " with name of the file in your terminal

## 4. Input your data... then ejoy the cool 2D visuals!

 

Responsibilities/Tasks Completed by Each Member 

Natsuki Abe took leadership over the code writing, but all members had view and contribution to programming. Tristan Janisse took leadership over mathematical computation, but everyone participated in completing that portion. Jamie Graham took leadership over documentation, but everyone contributed and added to the completed work. It was a solid team effort. 

System Performance Context Description 

The software used include PyCharm, and Python 2.7. The libraries necessary are Matplotlib, Numpy, and Scipy. To be able to use this software, the system requires an OS that meets the requirements of Python 2.7 installed on their computer. The user can execute the python file using the Python command in their terminal at that point. The main library that this solution is using is called odeint which is a powerful C++ library that is known for high performance in terms of accuracy, efficiency, and speed. The performance is competitive with plain C and Fortran90 code as the performance measured as runtime required to perform 200,000 Runge-Kutta4 steps for the Lorenz system.  When tested on Intel Hardware(Core i5 and Xeon E5) the applications have basically equivalent performance. This proves odeint gives the competitive performance needed for our solution to help our users. The library is also designed proficiently with a modularized design that has high flexibility for abstraction and modularization, with no added run-time costs. (Mulansky, M., & Ahnert, K.). 

Specific Problem Solve 

This project is using an odeint to calculate and visualize the rate of return based on a user’s input of an amount of money. For example, if you invest $10,000 and you get a 5% rate of return on the investment, you would make $500. When you add that to the initial principal, your capital grows to $10,500. The next year, you would get $525 and add that to $10,500, your capital grows to $11,025. The purpose is to plot the amount of money versus time to help the user determine compound interest. This mathematical application and computing solution could be used to help inform the user of how their money is being compounded. This could be set up for the user to use personally, for professionals to advice their clients, or for any other financial use case. 

Mathematical Approach for Solving it 

The mathematical approach for solving this problem is finding the derivative of the rate of compound interest multiplied by the amount of money over the course of time. This can be written out mathematically as so: 

    dS(t)dt=r∗S(t)
 

Where r is equal to rate, S is equal to money, and t is equal to time. 

     dSdt=rS
 

     1S dSdt=r
 

     1S dS=r dt
 

    ∫1S dS= ∫r dt


    lnS=rt+D


    S= ert+D


    S=Cert


    S(0)=Ce0


    S(0)=C
 

     Since S(0)=S0, we can also say that C=S0 


     S(t)= S0ert
 

Approach for Implementation 

One python package that is used in this project is Scipy that has capability for differential equations within odeint. Note, this stands for ordinary differential equation integration. The model keyword represents the return derivative value from requested y and t values within the dy/dt = model relationship (y,t). Y0 represents the initial conditions of differential states. T represents time points where solution should be returned with internal points that are used to maintain accuracy in the calculation.  

     Dy(t) / d(t) = r * y(t) 

Imported as such: 

From scipy.integrate import odeint 

Another python package used is Numpy. Numpy is popular scientific computing Python library that is used to create powerful N-dimensional array objects, broadcasting functions, linear algebra abilites, and tools to integrate C, C++, and Fortran code. (Numpy Documentation). 

Imported as such: 

Import numpy as np 

Finally, the last python package is Matplotlib. Matplotlib is a popular 2D plotting Python library that produces quality figure and interactive enviornments across platforms. It can used for Python, IPython shells, web application services, Jupyter notebook, and some graphical user interface toolkits. (Matplotlib Documentation). 

Imported as such: 

Import matplotlib.pyplot as plt 

Pseudo code for a returning dy/dt: 

Y0 = 5 (set initial condition) 

(Then return dy/dt) 

Function model (y,t): 

r= 0.3 

Dydt =  r * y 

Return dydt 

Set time points by setting t = np.linspace(0, 20) 

Then solve for ODEINT by calling function odeint: y = odeint(model, y0,t) 

Finally, plot results with plotly – plot T, y axis 

The predicted outcome of our graph is going to tthe mathematical relationship of y(t) and time as a curve. With these numbers, the curve would be going downward at a slight slope. 

To implement this algorithm, we are going to the using S for money.  

Flowchart 

This flowchart describes the movement of the code solution. 

 

Screenshots Depicting Key Phrases in Program Execution 

 

Page Break
 

References 

Matplotlib Documentation. (n.d.). Retrieved from https://matplotlib.org/ 

Mulansky, M., & Ahnert, K. (n.d.). Odeint library. Retrieved from  

http://www.scholarpedia.org/article/Odeint_library 

NumPy Documentation. (n.d.). Retrieved from https://numpy.org/ 

 
