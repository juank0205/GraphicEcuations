import numpy as np

#Module that includes definitions for functions used in the main program
def square(x:int, a:int, b:int, c:int)->int:
    return a*x**2 + b*x + c

#Evals a string with a list of values to be used as x inside the function
def evalString(string:str, xValues:list)->list:
    return eval(string, {'x': xValues})