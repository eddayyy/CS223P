# Author: Eduardo Nunez
# Author email: eduardonunez@csu.fullerton.edu

def perimeter(*, length = 0, width = 0):
    l = length
    w = width
    h = 2 * l + 2 * w
    return h

def area(*, length = 0 , width = 0):
    return length * width