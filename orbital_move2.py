import scipy.integrate as sc
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# =============================================================================
#
# =============================================================================
mu = 3.986 * 10**14
Re = 6371*10**3
pi = np.pi


# =============================================================================
H = 400e3
r = H+Re
T = 2*pi*(r**3/mu)**0.5
v_circ = (mu/r)**0.5
e = 0
O = w = 0
x0, y0, z0 = r, 0, 0
vx0, vy0, vz0, = 0, v_circ, 0

# =============================================================================
#
# =============================================================================
def fun(F, t):
    x, y, z = F[0], F[1], F[2]
    vx, vy, vz = F[3], F[4], F[5]
    r = (x**2 + y**2 + z**2)**0.5
    return vx, vy, vz, -mu*x/r**3, -mu*y/r**3, -mu*z/r**3

F0 = np.array([x0, y0, z0, vx0, vy0, vz0])
t = np.arange(0,T*5,60)
G = sc.odeint(fun, F0, t).T
X, Y, Z = G[0], G[1], G[2]
R = (X**2 + Y**2 + Z**2) ** 0.5

print(G)
ax = plt.figure().add_subplot(111, projection='3d')
ax.plot(X, Y, Z)
plt.show()