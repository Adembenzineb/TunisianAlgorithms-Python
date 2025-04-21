def pi_Calcul():
    pi = 3/4
    pi1 = pi
    i = 2
    sig = 1
    while  not( 0.0001 <= pi - pi1 <= 0.01):
        pi1 = pi
        pi += 1/ (i*i+1*i+2)*sig
        i += 2
    return pi
print(str(pi_Calcul()))