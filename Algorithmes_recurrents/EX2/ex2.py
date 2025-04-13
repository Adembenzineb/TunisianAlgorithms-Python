def somme(x,a,n):
    s = 0
    sig = -1
    for i in range (1,n,2):
        s += ( puissance(x*i)/ puissance(a*i-1) ) * sig
        sig *= -1
    return sig
def puissance(x,p):
    res = 1
    for i in range (1,p) :
        res *= x
    return res