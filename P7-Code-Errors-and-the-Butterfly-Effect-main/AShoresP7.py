#Asher Shores
#Dr. Ricardo Citro
#This is my own work

#Differential Equations:
# x' = o(y-x)
# y' rx - y - xz
# z' xy - bz

#Implementation
#Implement model and solves (lorenz attractor)

import numpy as np                  #import lib numpy as np for math
import matplotlib.pyplot as plt     #import lib matplotlib to graph
from mpl_toolkits.mplot3d import Axes3D #import the 3d plot thingy

#Set values for s, r, and b as given in documentation
#Return x,y,z-dot values for partials at point x, y, z

def lorenz(x, y, z, s=10, r=28, b=2.667):
    '''
    Given:
       x, y, z: a point of interest in three dimensional space
       s, r, b: parameters defining the lorenz attractor
    Returns:
       x_dot, y_dot, z_dot: values of the lorenz attractor's partial
           derivatives at the point x, y, z
    '''
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot


dt = 0.01           #step size
num_steps = 10000   #number of steps
#As per standard

#Need one more for the initial values
xs = np.empty(num_steps + 1)            #creates an empty x space
ys = np.empty(num_steps + 1)            #creates an empty y space
zs = np.empty(num_steps + 1)            #creates an empty z space
ts = np.linspace(0, 100, num_steps + 1) #creates an empty t space

def plot_Graph(si, ri, bi):
    # Set initial values
    xs[0], ys[0], zs[0] = (1., 1., 1.05)  #set the initial x, y, z values

    #Step through "time", calculating the partial derivatives at the current point and using them to estimate the next point
    for i in range(num_steps):
        x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i], s = si, r = ri, b = bi)   #set the x, y, z values from the lorenz function
        xs[i + 1] = xs[i] + (x_dot * dt)                                            #input x value into the xspace
        ys[i + 1] = ys[i] + (y_dot * dt)                                            #input y value into the xspace
        zs[i + 1] = zs[i] + (z_dot * dt)                                            #input z value into the xspace

    fig = plt.figure(1)             #create the figure to plot the 3d graph
    ax = fig.gca(projection='3d')   #create the 3d graph

    ax.plot(xs, ys, zs, lw=0.5)         #plot the spaces
    ax.set_xlabel("X Axis")             #x axis 
    ax.set_ylabel("Y Axis")             #y axis 
    ax.set_zlabel("Z Axis")             #z axis 
    ax.set_title("Lorenz Attractor")    #title

    plt.show()          #show the graph


#Plots
def plots():

    arrivalRate = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    serviceDuration = [2.22,1.76,2.13,0.14,0.76,0.70,0.47,0.22,0.18,2.41,0.41,0.46,1.37,0.27,0.27]
    serviceStartTime = [1,3.22,4.98,7.11,7.25,8.01,8.71,9.18,9.4,10,12.41,12.82,13.28,14.65,15]
    exitTime = [3.22,4.98,7.11,7.25,8.01,8.71,9.18,9.4,9.58,12.41,12.82,13.28,14.65,14.92,15.27]
    timeInQueue = [0,1.22,1.98,3.11,2.25,2.01,1.71,1.18,0.4,0,1.41,0.82,0.28,0.65,0]
    numberInSystem = [0,1,2,2,2,3,4,3,2,0,1,2,1,1,0]
    numberInQueue = [0,0,1,1,1,2,3,2,1,0,0,1,0,0,0]

    plt.title("Service Duration Vs Arrival Rate")
    plt.plot(arrivalRate, serviceDuration)
    plt.xlabel('Arrival Time')
    plt.ylabel('Service Duration')
    plt.show()

    plt.title("Service Start Time Vs Arrival Time")
    plt.plot(arrivalRate, serviceStartTime)
    plt.xlabel('Arrival Time')
    plt.ylabel('Service Start Time')
    plt.show()

    plt.title("Exit Time Vs Arrival Time")
    plt.plot(arrivalRate, exitTime)
    plt.ylabel('Arrival Time')
    plt.ylabel('Exit Time')
    plt.show()

    plt.title("Time in Queue Vs Arrival Time")
    plt.plot(arrivalRate, timeInQueue)
    plt.xlabel('Arrival Time')
    plt.ylabel('Time in Queue')
    plt.show()

    plt.title("Number in System Vs Arrival Time")
    plt.plot(arrivalRate, numberInSystem)
    plt.xlabel('Arrival Time')
    plt.ylabel('Number in System')
    plt.show()

    plt.title("Number in Queue Vs Arrival Time")
    plt.plot(arrivalRate, numberInQueue)
    plt.xlabel('Arrival Time')
    plt.ylabel('Number in Queue')
    plt.show()



#Interactive part as indicated

s = 10
r = 28
b = 2.667
#Set the same initial conditions as above

plot_Graph(s, r, b) #run the function with initial conditions

#allow for user input and then a while loop to run continously for new values as set
#by the potential user

plots()

go = input("Run With New Values? (y | n): ")
#user input variable to run again

while(go == 'y'):  #loop true for each time user wants to run the program with new vars
                   #else the program ends
                   
    s = float(input("Input s value (default 10): "))
    r = float(input("Input r value (chaotic at 28): "))
    b = float(input("Input b value (default 2.667): "))
    #new values for the variables

    plot_Graph(s, r, b)                          #plot with new user values
    go = input("Run Lorenz Function (y | n): ")
    #user input variable again to maintain the loop
