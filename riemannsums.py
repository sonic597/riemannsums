a = 0 #lower bound
b = 1 #upper bound
def f(x): #function to integrate
    return x**2
rects = 10000 # number of rectangles used in the approximation

width = (b-a)/rects
ls = 0
us = 0 
x = a

for i in range(rects):
    ls += f(x)*width
    us += f(x+width)*width
    x += width

print("integral of f(x) between: ", ls, "and", us)