def Calcul_e():
    e = 1
    i = 1
    e2 = 0
    p = 1
    while abs(e - e2) > 0.0001 :
        e2 = e
        e += 1 / p
        i += 1
        p *= i
    return e
print( str(Calcul_e()))