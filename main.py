from functions import plotEuler, plotFunction

#Limits for the plot axes
xmin, xmax, ymin, ymax = -10, 10, -10, 10
npoints = 20
precision = 10
tickrate = 2

def main():
    #Main menu
    isLooping = True
    while isLooping:
        option = int(input('''
1. Plot a function
2. Euler method
0. Exit

Select an option:'''))
        if option == 1:
            plotFunction(xmin, xmax, ymin, ymax, npoints, tickrate)
        elif option == 2:
            plotEuler(xmin, xmax, ymin, ymax, tickrate)
        elif option == 0:
            isLooping = False

main()