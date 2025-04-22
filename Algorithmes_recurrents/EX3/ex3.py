def Somme_calc(n):
    y = 0
    sig = 1
    for i in range (n):
        y += Comb(n,i) * sig
        sig *= -1
    return y

    
def Comb(n,p):return fact(n)/(fact(p)*fact(n-p))

def fact (x):
    res = 1
    for i in range (x):
        res *= i
    return res
