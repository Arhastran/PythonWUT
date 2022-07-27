import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib import animation



def pendulum(u,t):
    du = np.zeros(2)
    du[0] = u[1]
    du[1] = -0.1*u[1]- np.sin(u[0]) #powyżej wsp. tarcia razy omega odjąć g/l*sin(theta)
    return du


def update(i):
    plt.clf() #czyści cały rysunek
    plt.axis([-2,2,-2,2])
    plt.plot([0,x1[i]],[0,y1[i]])
    plt.plot([x1[i]],[y1[i]], 'ro')

u0 = [np.pi/2, 0] #warunki początkowe
tmax = 1000 #całkowity czas symulacji
N = 2000 #liczba kroków symulacji
t = np.linspace(0, tmax, N) #tablica czasów


wynik = odeint(pendulum, u0, t)
theta = wynik[:,0]
x1 = np.sin(theta)
y1 = -np.cos(theta) #bo układ odwrócony, góra dół

fig = plt.figure()
anim = animation.FuncAnimation(fig, update, frames = N, interval = 20)
plt.show()










