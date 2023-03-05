from plotting import setPlotStyle, plot, show
import numpy as np
import math

# Module that includes definitions for functions used in the main program

# Function definitions
# Quadratic function
def quadratic(x: int, a: int, b: int, c: int) -> int:
    return a*x**2 + b*x + c

# Linear function
def linear(x: int, a: int, b: int) -> int:
    return a*x + b

# Plot a linear function where m is the slope and b is the y-intercept
def plotLinear(m, b, xRange):
    y = linear(xRange, m, b)
    plot(xRange, y, '#FF0000', 2)

# Plot a line segment using its initial and final points
def plotStep(x, y, xi, yi):
    plot([x, xi], [y, yi], '#FF0000', 2)

# Evals a string with a list of values to be used as x inside the function
def evalString(string: str, xValues: list) -> list:
    return [float(string)]*len(xValues) if string.isdigit() else eval(str(string), {'x': xValues, 't': xValues, 'math': math})


# Plot a function
def plotFunction(xmin, xmax, ymin, ymax, npoints):
    # Get the function from the user
    string = input("Enter a function: ")

    # Create a list of x values from xmin to xmax with npoints elements
    # Y list is created by evaluating the function with the x list
    x = np.linspace(xmin, xmax, npoints)
    try:
        y = evalString(string, x)
    except: 
        print("Invalid function")
        return
    
    # Plot the function
    setPlotStyle(xmin, xmax, ymin, ymax)
    plot(x, y, '#FF0000', 2)
    show()

# Plot a function using eulers method
def plotEuler(xmin, xmax, ymin, ymax):
    # Get the function from the user and the initial values

    try:
        string = input("Enter a function dy/dt = ")
        xo = float(input("Enter the initial value of x: "))
        yo = float(input("Enter the initial value of y: "))
        step = float(input("Enter the step size: "))
        setPlotStyle(xmin, xmax, ymin, ymax)
        # Set the x values to the right of the initial point
        xRange = np.arange(xo, xmax, step)
    except:
        print("Invalid data\n")
        return

    # Calculate the y values using eulers method and plotting the line segments
    yi = yo
    try:
        for i in range(len(xRange)-1):
            m = evalString(string, xRange[i])
            plotStep(xRange[i], yi, xRange[i+1], yi+(m*step))
            yi += m*step
    except:
        print("Invalid function\n")
        return

    # Same process but to the left of the initial point
    xRange = np.arange(xo, xmin, step*(-1))
    yi = yo
    try:
        for i in range(len(xRange)-1):
            m = evalString(string, xRange[i])
            plotStep(xRange[i], yi, xRange[i+1], yi-(m*step))
            yi -= m*step
    except:
        print("Invalid function")
        return

    show()
