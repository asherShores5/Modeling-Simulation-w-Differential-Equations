#Asher Shores
#Professor Citro
#CST-305
#September 19, 2021
#This is my own work

#Comments here will depict brief overview of what each line represents
#Substantive commentary can be found in attached word document

#ODE --> dx/dt = m/t 
#Throughput is equivalent to the ratio of material over unit time
#-----------------------------------------------------------------#

import numpy as np
#imports numpy to be used to define numerical space

from scipy.integrate import odeint 
#utilizes odeint from scipy lib to actually solve and heavy lift ODE

import matplotlib.pyplot as pt
#imports matplot lib for visual representation at end

#abstracted function inheriting from model class
def model(x,t,m):   
  dxdt = m / t
  #ODE is equivalent to ratio of materials per unit time
  return dxdt
  #return the resulting ODE


x0 = 5
# Sets up the initial condition

t = np.linspace(1,25)
#set the horizontal axis with necessary scale

# solve ODE with odeint
m = 5                               #for 5 given material
x1 = odeint(model,x0,t,args=(m,))   #Calculate result & store in x1
m = 10                              #for 10 given material
x2 = odeint(model,x0,t,args=(m,))   #Calculate result & store in x2
m = 15                              #for 15 given material
x3 = odeint(model,x0,t,args=(m,))   #Calculate result & store in x3
m = 20                              #for 20 given material
x4 = odeint(model,x0,t,args=(m,))   #Calculate result & store in x4

# plot results
pt.plot(t,x1,'r-',linewidth=2,label='m=5')
#results for m = 5
pt.plot(t,x2,'b--',linewidth=2,label='m=10')
#results for m = 10
pt.plot(t,x3,'y--',linewidth=2,label='m=15')
#results for m = 15
pt.plot(t,x4,'g:',linewidth=2,label='m=20')
#results for m = 20

pt.xlabel('Time')
#x-axis label as time
pt.ylabel('Throughput')
#y-axis label as Throughput
pt.legend()
#display graph legend
pt.show()
#plots the plot