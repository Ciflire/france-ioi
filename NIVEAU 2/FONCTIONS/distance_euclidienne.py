from math import *


def module(x1, x2, y1, y2):
    modulec = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
    module = sqrt(modulec)
    print(module)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

module(x1, x2, y1, y2)
