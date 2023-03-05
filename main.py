from functions import plotEuler, plotFunction

#Limits for the plot axes
xmin, xmax, ymin, ymax = -10, 10, -10, 10
npoints = 200

def setPlotLimits():
    global xmin, xmax, ymin, ymax
    try:
        xmin = float(input("Enter the minimum x value: "))
        xmax = float(input("Enter the maximum x value: "))
        ymin = float(input("Enter the minimum y value: "))
        ymax = float(input("Enter the maximum y value: "))
    except:
        print("Invalid data")

def main():
    #Main menu
    isLooping = True
    while isLooping:
        try:
            option = int(input('''
1. Plot a function
2. Euler method
3. Set plot limits
0. Exit

Select an option:'''))
        except:
            print("Invalid option")
            continue

        if option == 1:
            plotFunction(xmin, xmax, ymin, ymax, npoints)
        elif option == 2:
            plotEuler(xmin, xmax, ymin, ymax)
        elif option == 3:
            setPlotLimits()
        elif option == 0:
            isLooping = False

main()
