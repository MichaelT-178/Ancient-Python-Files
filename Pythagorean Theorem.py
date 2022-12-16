# Created April 8th 2021

import math

def pythagorean_theorem(a, b):
    print(f"\nIf A is {num1} and B is {num2}, then C is...")
    csquared = ((a**2)+(b**2))
    c = math.sqrt(csquared)
    realc = "{:.2f}".format(c)
    return realc


num1 = int(input('Please enter a number for A: '))
num2 = int(input('Please enter another number B: '))
print(pythagorean_theorem(num1, num2))   
