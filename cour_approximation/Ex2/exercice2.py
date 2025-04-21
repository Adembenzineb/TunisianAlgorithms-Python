from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication,QMessageBox,QTableWidget,QTableWidgetItem

def play():
    
    eps = f.zone.text()
    
    if eps == "" :
        QMessageBox.critical(f,"Error","Veuiller donner epsilone")
    else:
        vlop = epsilon(float(eps))
        f.res.setText(str(vlop))
        


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

def epsilon(x):
    n = 0
    res = ( puissance(n+1,2) *puissance(2,fact(n)) )/ fact(2*n +1)
    res1 = 0
    while abs (res - res1) > x :
        res1 = res
        res += ( puissance(n+1,2) *puissance(2,fact(n)) )/ fact(2*n +1)
        n += 1
        print(res)
    return res



app = QApplication([])
f = loadUi ("ex2qt.ui")
f.show()
f.button.clicked.connect (play)
app.exec_()

