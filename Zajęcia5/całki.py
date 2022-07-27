import numpy as np
import time
import scipy.integrate as calka

def fun(x):
    return np.sin(x)



def trapez(f,a,b,h):
    x = np.arange(a,b+h,h) #array, z dodatkowym +h bo krańce giną bez tego
    s = np.sum(f(x))-0.5*f(a)-0.5*f(b) # tutaj odejmujemy powtórzone krańce
    return h*s




a=0
b=np.pi
h=(b-a) / 10000000
t1 = time.perf_counter()
c=trapez(fun,a,b,h)
print("Wynik: ",c)
t2 = time.perf_counter()
t3 = t2-t1
print("Czas wykonywania programu: ", t3)

t4 = time.perf_counter()
calk = calka.quad(fun,a,b)
t5 = time.perf_counter()
t6 = t5-t4
print("Inny sposob z biblioteki: ", calk)
print("Czas tej metody: ", t6)


calka.romberg(fun,a,b,show=True) #całkowanie metoda Romberga