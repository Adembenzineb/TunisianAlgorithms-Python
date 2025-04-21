def sinuse(x):
    res = 0
    sig = 1
    res1 = 1
    p = 0
    while abs (res - res1) > 0.0001 :
        res1 = res
        res += (puissance(x,p*2+1) / fact(p*2+1))*sig
        sig *=  -1
        p += 1
    return res

def puissance(n,p):
    res = 1
    for i in range (n):
        res *= p
    return res

def fact(n):
    res = 1
    for i in range (1,n):
        res *= i
    return res

print(sinuse(80))