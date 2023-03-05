import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

#import modules
from functions import *


#Setting the plotter window style
def setPlotStyle(xmin, xmax, ymin, ymax):
    fig, ax = plt.subplots()
    fig.set_size_inches(15, 15)
    fig.patch.set_facecolor('#FFFFFF')
    
    #Set axes limits and aspect ratio
    ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect='equal')

    #Set axes position and visibility to look like a cartesian plane
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    #Set axes ticks style
    ax.set_xlabel('$t$', size=14, x=1.02, labelpad=-24) 
    ax.set_ylabel('$y$', size=14, y=1, labelpad=-30, rotation=0)

    #Set axes ticks
    ax.xaxis.set_major_locator(ticker.MaxNLocator(16))
    ax.yaxis.set_major_locator(ticker.MaxNLocator(16))
    yticks = ax.get_yticks()
    ax.set_yticks([tick for tick in yticks if tick != 0])
    ax.tick_params(axis='x', labelrotation=-45)

    #Create a grid (decoration)
    ax.grid(which='both', color='#a5a5a5', linestyle='-', linewidth=1, alpha=0.5)

def plot(x:list, y:list, color:str, linewidth:int):
    plt.plot(x, y, color=color, linewidth=linewidth)

def show():
    plt.show()
