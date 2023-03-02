import numpy as np
import matplotlib.pyplot as plt

#import modules
from functions import *

#Limits for the plot axes
xmin, xmax, ymin, ymax = -10, 10, -10, 10
tickrate = 2

#Setting figure size and background color
fig, ax = plt.subplots(figsize=(7, 7))
fig.patch.set_facecolor('#FFFFFF')

#Set axes limits and aspect ratio
ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect='equal')

#Set axes position and visibility to look like a cartesian plane
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

#Set axes ticks style
ax.set_xlabel('$x$', size=14, x=1.02, labelpad=-24) 
ax.set_ylabel('$y$', size=14, y=1, labelpad=-30, rotation=0)
plt.text(0.499, 0.499, r"$0$", ha='right', va='top', 
         transform=ax.transAxes,
         horizontalalignment='center',
         fontsize=12)

#Set axes ticks
x_ticks = np.arange(xmin, xmax+1, tickrate)
y_ticks = np.arange(ymin, ymax+1, tickrate)
ax.set_xticks(x_ticks[x_ticks != 0])
ax.set_yticks(y_ticks[y_ticks != 0])
ax.set_xticks(np.arange(xmin, xmax+1), minor=True)
ax.set_yticks(np.arange(ymin, ymax+1), minor=True)

#Create a grid (decoration)
ax.grid(which='both', color='#a5a5a5', linestyle='-', linewidth=1, alpha=0.5)

#Function
string = input("Enter a function: ")

x = np.linspace(xmin, xmax, 200)
y = evalString(string, x)

#Plot the function
plt.plot(x, y, color='#FF0000', linewidth=2)

plt.show()