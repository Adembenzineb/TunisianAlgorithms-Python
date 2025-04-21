def volume_max(pas):
    x = 0
    xop = x
    vmax = f(x)
    while x < 15 :
        x+= pas
        v = f(x)
        if v > vmax :
            vmax = v
            xop = x
    
    print("xop :",str(xop))
    print("vmax :",str(vmax))
    
def f(x):
    return 2*x*x*x -60*x*x + 450*x


def saisir():
    pas = float(input("donner le pas"))
    while not(0.001 <= pas <= 0.01):
        pas = float(input("donner le pas"))
    return pas
    
pas = saisir()
pas = float(input("donner le pas"))
volume_max(pas)
