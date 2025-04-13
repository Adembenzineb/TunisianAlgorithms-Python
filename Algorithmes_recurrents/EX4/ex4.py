def binome(a,b,n):
    s = 0
    for i in range (n):
        s += Comb(n,i)*puissance(a,n-i)*puissance(b,i)
    return s

def puissance(x,p):
    res = 1
    for i in range (1,p) :
        res *= x
    return res

def Comb(n,p):return fact(n)/(fact(p)*fact(n-p))

def fact (x):
    res = 1
    for i in range (x):
        res *= i
    return res