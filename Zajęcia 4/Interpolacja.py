import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import scipy.interpolate as interp

x = np.array([0,1,2,3,4])
y = np.array([12,14,52,39,58])

cs = interp.CubicSpline(x,y,bc_type="natural") #typ warunku z wykładu, daje 1 i 2 pochodna = 0

xfit = np.linspace(-2,6,100)
yfit = cs(xfit)
plt.plot(x,y,'ro')
plt.plot(xfit,yfit)
plt.show()