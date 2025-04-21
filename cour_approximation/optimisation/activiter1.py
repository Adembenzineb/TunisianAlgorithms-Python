from math import*
def optimisation_1(pas):
    x = 0
    xop = x
    smax = f(x)
    while x <= 3/2 :
        x += pas
        s = f(x)
        if s > smax:
            xop = x
            smax = s
            
    print("xop: ",xop , "smax : ",smax)
    return smax

def f (x):
    return 2 * sqrt(3) * x * x + 3 * sqrt(3) * x

optimisation_1(1)