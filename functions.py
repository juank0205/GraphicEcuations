from plotting import setPlotStyle, plot, show
import numpy as np

# Module that includes definitions for functions used in the main program


def quadratic(x: int, a: int, b: int, c: int) -> int:
    return a*x**2 + b*x + c


def linear(x: int, a: int, b: int) -> int:
    return a*x + b


def plotLinear(m, b, xRange):
    y = linear(xRange, m, b)
    plot(xRange, y, '#FF0000', 2)


def plotStep(x, y, xi, yi):
    plot([x, xi], [y, yi], '#FF0000', 2)

# Evals a string with a list of values to be used as x inside the function


def evalString(string: str, xValues: list) -> list:
    return eval(string, {'x': xValues})

# Plot a function


def plotFunction(xmin, xmax, ymin, ymax, npoints, tickrate):
    string = input("Enter a function: ")
    x = np.linspace(xmin, xmax, npoints)
    y = evalString(string, x)
    setPlotStyle(xmin, xmax, ymin, ymax, tickrate)
    plot(x, y, '#FF0000', 2)
    show()

# Plot a function using eulers method


def plotEuler(xmin, xmax, ymin, ymax, tickrate):
    string = input("Enter a function dy/dt = ")
    xo = float(input("Enter the initial value of x: "))
    yo = float(input("Enter the initial value of y: "))
    step = float(input("Enter the step size: "))

    setPlotStyle(xmin, xmax, ymin, ymax, tickrate)

    xRange = np.arange(xo, xmax, step)
    yi = yo
    for i in range(len(xRange)-1):
        m = evalString(string, xRange[i])
        plotStep(xRange[i], yi, xRange[i+1], yi+(m*step))
        yi += m*step

    xRange = np.arange(xo, xmin, step*(-1))
    yi = yo
    for i in range(len(xRange)-1):
        m = evalString(string, xRange[i])
        plotStep(xRange[i], yi, xRange[i+1], yi-(m*step))
        yi -= m*step
    show()
