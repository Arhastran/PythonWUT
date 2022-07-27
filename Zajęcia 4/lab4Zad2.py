"""
Adam Ignaciuk
Program na zajęcia czwarte
Zadanie 2 - funkcje sklejane
"""


import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import scipy.interpolate as interp

def fun(x,a,b,c,d):
    return a*x**3+b*x**2+c*x+d


x = np.array([0,1,2,3,4])
y = np.array([12,14,52,39,58])

cs = interp.CubicSpline(x,y,bc_type="natural") #typ warunku z wykładu, daje 1 i 2 pochodna = 0

xfit = np.linspace(-2,6,100)
yfit = cs(xfit)
plt.plot(x,y,'ro')
plt.plot(xfit,yfit)

krok = 0
while (krok<4):
    a=cs.c[0][krok]
    b=cs.c[1][krok]
    c=cs.c[2][krok]
    d=cs.c[3][krok]
    y=fun((xfit-krok),a,b,c,d)
    plt.plot(xfit,y,label=f"{krok+1} funkcja")
    krok += 1


plt.ylim(-100, 100)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Różne funkcje sklejane")
leg=plt.legend()
plt.show()