import numpy as np
from math import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
from matplotlib.figure import Figure

def F(u, t):
    return np.sin(0.1*u+t)
N=513
NT=1000
dt=0.01
D = 0.04

x = np.linspace(0,2*pi,N)
u0 = np.sin(5*x)
fu = np.fft.fft(u0)
u = u0
z=np.empty((NT,N), dtype=float)
h= 2*pi/N

l = np.empty(N)
for k in range(N//2+1):
    l[k] = 2*D/(h**2) * (1 - cos(k*h/2))
    l[-k] = l[k]

for t in range(1, NT):
    us = u
    fus = fu
    for s in range(3):
        F1 = F(u, (t-1)*dt)
        F2 = F(us, t*dt)
        f = np.fft.fft(F1+F2)
        fus = ((2-dt*l)*fu + dt*f)/(2 + dt*l)
        #print(fu)
        us = np.fft.ifft(fus)
    u = us
    fu = fus
    z[t] = np.real(us)

#plt.imshow(z.transpose())
#plt.show()

fig = plt.figure()
ax = plt.axes(xlim=(0, 20), ylim=(-2, 2000))
line, = ax.plot([], [], lw=3)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    x = np.linspace(0, 4, 513)
    y = i*z[t]
    line.set_data(x,y)
    return line,

anim = FuncAnimation(fig, animate, init_func=init,
                               frames=2000, interval=10, blit=True)

plt.grid(True)
plt.show()



