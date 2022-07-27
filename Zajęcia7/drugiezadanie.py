"""
Uwaga ten kod TEŻ chyba działa
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sp


def step(spins, M, T):
    for i in range(N):
        x = np.random.randint(N)
        sum = np.sum(spins) - spins[x]
        delthaE = 2 * spins[x] * sum
        if  delthaE <= 0 or np.random.rand() < np.exp(- delthaE / T):
            spins[x] *= -1
            M += 2 * spins[x]
    return spins, M

def tanh(m, T):
    return np.tanh((N-1)*m/T)-m


nsteps = 10
N = 1000
T = 100
M = N

Mag = list()
Mag2 = list()

spins = np.ones(N)
m=np.zeros(nsteps)

while (T<2000):
    for t in range (nsteps):
        spins, M = step(spins,M,T)
        m[t] = M/N #magnetyzacja
    Mag.append(m[9]) #dopisuje do listy
    Mag2.append(sp.root_scalar(tanh, args=(T), method='secant', x0=1, x1=2).root) #szachermacher z biblioteki
    T+=50

plt.figure("Wykres magnetyzacji")
Twykres = range(100, 2000, 50)
plt.axis([0, T, -1.1, 1.1])
plt.plot(Twykres, Mag, label="Krzywa doświadczalna")
plt.plot(Twykres, Mag2, label="Krzywa teoretyczna")
plt.legend()
plt.show()


