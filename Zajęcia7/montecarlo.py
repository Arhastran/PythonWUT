import numpy as np
import matplotlib.pyplot as plt


def step(spins, M, T):
    for i in range(N):
        x = np.random.randint(N) #losuję spin do potencjalnej zmiany
        suma = np.sum(spins) - spins[x]
        DeltaE = 2*spins[x]*suma
        if DeltaE <= 0 or np.random.rand() <np.exp(-DeltaE/T): #metoda Metropolisa
            spins[x] *= -1
            M += 2*spins[x]
    return spins,M


#Model Isinga
N = 1000 #rozmiar układu
nsteps = 100 #liczba kroków symulacji
#przyjmujemy stałą Boltzmanna = 1
T = 1500 #temperatura. Około 1500 paramagentyk. Przy 500 fluktuuje wokół zera
spins = np.ones(N) #tablica spiów, wszystko do góry bo zakładamy na początek ferromagnetyk
M = N #magentyzacja
m = np.zeros(nsteps)

for t in range (nsteps):
    spins, M = step(spins,M,T)
    m[t] = M/N #magnetyzacja

fig = plt.figure()
plt.axis([0 , nsteps, -1.1, 1.1])
plt.plot(range(nsteps), m)
plt.show()