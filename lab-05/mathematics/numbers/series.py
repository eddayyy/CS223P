# Author: Eduardo Nunez
# Author email: eduardonunez@csu.fullerton.edu

def sum(*, list = []):
    z = list
    y = 0
    for item in z:
        y += item
    return y

def average(*, list = []):
    x = list
    avgoflist = sum(list = x) / len(x)
    return avgoflist