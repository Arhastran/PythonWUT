"""
Uwaga kod chyba działa, ale do końca nie byłem pewien bo miałem problemy podczas pisania
"""


import numpy as np
import matplotlib.pyplot as plt

def step(spins, M, T):
    for i in range(N):
        x = np.random.randint(N)
        sum = np.sum(spins) - spins[x]
        delthaE = 2 * spins[x] * sum
        if  delthaE <= 0 or np.random.rand() < np.exp(- delthaE / T):
            spins[x] *= -1
            M += 2 * spins[x]
    return spins, M


T = 100
nsteps = 10
N = 1000

M = N
Mag = list() #lista na wykres
spins = np.ones(N)
m=np.zeros(nsteps)

while (T<2000):
    for t in range (nsteps):
        spins, M = step(spins,M,T)
        m[t] = M/N #magnetyzacja
    Mag.append(m[9]) #dopisuje do listy
    T+=50


fig = plt.figure("Wykres magnetyzacji")
plt.xlabel("T")
plt.ylabel("Magnetyzacja")
plt.axis([0, T, -1.1, 1.1]) # tutaj miałem problem i nie umiałem naprawić
Twykres = range(100, 2000, 50) #chyba naprawiłem
plt.plot(Twykres, Mag)
plt.show()
