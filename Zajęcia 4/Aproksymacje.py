import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt


def fun(x,a,b,c,d):
    return a*x**3+b*x**2+c*x+d

x = np.linspace(-5,5,num=20)
y = fun(x,2,-5,4,-1) + 30*np.random.normal(size=20)

params, covariance  = opt.curve_fit(fun,x,y)
#np.set_printoptions(precision=3, suppress=True) #ustawia ładnie tablice
plt.plot(x,y,'ro') #ro rysuje czerwony makrerem kropki i nie łaczy linią
plt.plot(x,fun(x,*params))
plt.plot(x,fun(x,2,-5,4,-1)) #różnica dopasowania, inny wielomian z innych parametrów. Oznacza, że wyraz wolny jest obarczony ogromnym błędem
plt.show()