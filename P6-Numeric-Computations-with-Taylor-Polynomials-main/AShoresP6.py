#Asher Shores
#Dr. Ricardo Citro
#This is my own work
#November 30th, 2021

#Differential Equations:
# Pt 1 a) y" -2xy' +x^2y = 0; y(0) = 1, y'(0) = -1
# b) near x = 3; y" - (x-2)y' + 2y = 0; y(3) = 6, y'(3) = 1

# Pt 2 ) (x^2 + 4)y" + y = x; x = 0

import time                         #import time for time
import numpy as np                  #import lib numpy as np for math
import matplotlib.pyplot as plt     #import lib matplotlib to graph
from scipy.special import factorial #import factorial function
from scipy.integrate import odeint          #import odeint from scipy

#pt 1 equation a
def p1a(x):
    y0 = 1              # Val of 1st term for final y(x)
    y1 = -x             # Val of 2nd term for final y(x)
    y2 = 0              # Val of 3rd term for final y(x)
    y3 = -1 / 3 * pow(x, 3)     # Val of 4th term for final y(x)
    y4 = -1 / 12 * pow(x, 4)    # Val of 5th term for final y(x)
    return  y0 + y1 + y2 + y3 + y4  #Returns as an equation
    
print("Value of y(x) for x = 3.5: ")
print(p1a(3.5))

#pt 1 equation b
def p1b(x):
    y0 = 6                      # Val of 1st term for final y(x)
    y1 = (x-3)                  # Val of 2nd term for final y(x)
    y2 = -11/2 * pow((x-3), 2)  # Val of 3rd term for final y(x)
    y3 = -12/6 * pow((x-3), 3)  # Val of 4th term for final y(x)
    y4 = -12 / factorial(4) * pow((x-3), 4)  # Val of 5th term for final y(x)
    return y0 + y1 + y2 + y3 + y4

#pt 2
def p2(x, a0, a1):
    i = a0 * (1 - (1 / 8) * pow(x, 2) + (1 / 128) * pow(x, 4) - (13 / 15360) * pow(x, 6) + (403 / 3440640) * pow(x, 8) - (7657 / 412876800) * pow(x, 10))
    #setting the first pt of the final equation
    j = a1 * (x - (1 / 24) * pow(x, 3) + (7 / 1920) * pow(x, 5) - (7 / 15360) * pow(x, 7) + (301 / 4423680) * pow(x, 9))
    #setting the second pt of the final equation
    return i + j    #returning the answer

dt = 0.02       #dt val to graph
steps = 10000   #steps to graph set at 10k

#graph space
xspace = np.linspace(-100, 100, steps)  #the xspace space
yspace_a = np.empty(steps)                  #y for pt 1 a
yspace_b = np.empty(steps)                  #y for pt 1 b
yspace_2 = np.empty(steps)                   #y for pt 2
    
#arrays to hold vals
for i in range(-10000, 10000):
    yspace_a[i] = p1a(i * dt)       #pt 1 a
    yspace_b[i] = p1b(i * dt)       #pt 1 b
    yspace_2[i] = p2(i * dt, 2, 2)   #pt 2


plt.title("Taylor a)")  #set title
plt.xlabel("x")         #label x
plt.ylabel("y")         #label y
plt.plot(xspace, yspace_a)  #plot
plt.show()              #show plot

plt.title("Taylor b)")  #set title
plt.xlabel("x")         #label x
plt.ylabel("y")         #label y
plt.plot(xspace, yspace_b)  #plot
plt.show()              #show plot

plt.title("Power Series")   #set title
plt.xlabel("x")             #label x
plt.ylabel("y")             #label y
plt.plot(xspace, yspace_2)       #plot
plt.show()                  #show plot
