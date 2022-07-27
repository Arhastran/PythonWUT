"""
Adam Ignaciuk
program na lab5: obliczanie całek

"""

import numpy as np
import time
import scipy.integrate as calka


def fun(x):
    return np.sin(x)



def trapez(f,a,b,h):
    x = np.arange(a,b+h,h) #array, z dodatkowym +h bo krańce giną bez tego
    s = np.sum(f(x))-0.5*f(a)-0.5*f(b) # tutaj odejmujemy powtórzone krańce
    return h*s




def roemberg (f,a,b,m):
    I=np.zeros((m,m+1), float) #przechowuje kolejne iteracje, dla trapezów i potem dla wzoru
    k=1 #kroki
    h=b-a #przedział
    for j in range (m):
        I[j,0] = trapez(f, a, b, h / 2 ** j)
        while (k < m-1):
            k += 1
            I[j,k] = ((4 ** k) * I[j + 1][k - 1] - I[j][k - 1]) / (4 ** k - 1)
    return I[j,0] #ostatnie rozwiązanie którego potrzebujemy
    # Uwaga - jeśli damy po prostu J, pokażą się wszstkie iteracje. Okazuje się, że mój terminal przybliża
    # wtedy rozwiązanie jako 2 już w 16 kroku.

a=0
b=np.pi
h=(b-a)/100000
m=20 #UWAGA, mój macbook przy >25 potężnie się zaciął. Wystarczy 18 iteracji, żeby prebić metodę trapezów która ma
    #przedział podzielony na 100000

print("##########################################################")

t1 = time.perf_counter()
x=roemberg(fun,a,b,m)
t2 = time.perf_counter()
print(f"Rozwiązanie metodą Roemberga przy {m} iteracjach: ",x)
print("Czas obliczeń: ", t2-t1)

print("##########################################################")

t3 = time.perf_counter()
y=trapez(fun,a,b,h)
t4 = time.perf_counter()
print("Rozwiązanie metodą trapezów ", y)
print("Czas obliczeń: ", t4-t3)

print("##########################################################")
t5 =(t2-t1)-(t4-t3)
print("Różnica w czasie Roemberg - trapezy: ", t5)

#Metoda trapezów jest odrobinę dokładniejsza przy podziałce kroku na 1 000 00, jednak robi się wtedy wolniejsza.