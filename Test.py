from pylab import *
from scipy import integrate

m = 25.0
q = 5.0
Ex = 0.0
Ey = 0.0
Ez = 0.1
Bx = 0.0
By = 0.0
Bz = 5.0

def solver(X, t0):
    vx = X[3]
    vy = X[4]
    vz = X[5]
    ax = q * (Ex + (vy * Bz) - (vz * By) ) /m
    ay = q * (Ey - (vx * Bz) + (vz * Bx) ) /m
    az = q * (Ez + (vx * By) - (vy * Bx) ) /m
    return [vx, vy, vz, ax, ay, az ]

pv0 = [0,0,0, 0,1,0]
t = arange(0, 50, 0.01)
pv = integrate.odeint(solver, pv0, t)

from mpl_toolkits.mplot3d import Axes3D
ax = Axes3D(figure())
ax.plot(pv[:,0], pv[:,1], pv[:,2])
ax.set_zlabel('Z axis')
show()