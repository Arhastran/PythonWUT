"""
Adam Ignaciuk
Program na zajęcia czwarte
Zadanie 1 - interpolacja
"""


import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

def fun2(x,a,b,c,d):
    return a*(np.sin(69+x))**3+np.exp(b)*(x**2)+c*x+np.e+d #to jest jakiś potwór

def fun3(x,a,b,c,d):
    return a*np.sin(b*x)*c*np.exp(-d*x**2)

def sad(x,a,b,c,d):
    return a*(np.sin(69+x))**3+(b)*(x**2)+c*x+np.e+(np.exp(1-d))**-1 # tu taki fajny łuczek



x = np.linspace(-20,20,num=49)
y = sad(x,8,-5,7,-6) + 30*np.random.normal(size=49)

params, covariance  = opt.curve_fit(sad,x,y)
plt.plot(x,y,'ro') #ro rysuje czerwony makrerem kropki i nie łaczy linią
plt.plot(x,sad(x,*params))
plt.plot(x,sad(x,8,-5,7,-6)) #różnica dopasowania, inny wielomian z innych parametrów. Oznacza, że wyraz wolny jest obarczony ogromnym błędem
plt.show()



