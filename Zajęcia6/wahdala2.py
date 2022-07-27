import numpy as np
from scipy.integrate import odeint
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib import animation



def pendulum(u,t):
    du = np.zeros(4) #wykorzystuje dwa dodatkowe miejsca w tablicy jako wartości dla drugiego wahadła
    du[0] = u[1]
    du[2] = u[3] #Theta 2
    du[1] = (-3*np.sin(u[0]) - np.sin(u[0]-2*u[2])-2*np.sin(u[0]-u[2]) * ((u[3]**2) + (u[1]**2) * np.cos(u[0] - u[2]))) / (3 -np.cos(2*u[0] - 2*u[2]))
    du[3] = (2*np.sin(u[0]-u[2]) * (2*(u[1]**2) + 2*np.cos(u[0]) + (u[3]**2) * np.cos(u[0]-u[2]))) / (3 - np.cos(2*u[0] - 2*u[2])) #Theta2 prim
    return du



def update(i):
    plt.subplot(2,1,1)
    plt.clf() #czyści cały rysunek
    plt.axis([-2,2,-2,2])
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.title("Double pendulum")
    plt.plot([0,x1[i]],[0,y1[i]], 'b-')
    plt.plot([x1[i]],[y1[i]], 'ro')
    plt.plot([x1[i], x2[i]], [y1[i], y2[i]], 'b-') #drugie wahadło zaczepione o pierwsze
    plt.plot([x2[i]], [y2[i]], 'ro')



u0 = [np.pi/2, 0,np.pi/2,0] #warunki początkowe
tmax = 1000 #całkowity czas symulacji
N = 2000 #liczba kroków symulacji
t = np.linspace(0, tmax, N) #tablica czasów

wynik = odeint(pendulum, u0, t)
theta = wynik[:,0]
theta2 = wynik[:,2]
x1 = np.sin(theta)
y1 = -np.cos(theta) #bo układ odwrócony, góra dół
x2 = x1 + np.sin(theta2)
y2 = y1 - np.cos(theta2) #bo układ odwrócony


fig = plt.figure()
anim = animation.FuncAnimation(fig, update, frames = N, interval = 20)


plt.show()






