import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
pi=3.14
def f(y, t,params):
	y1, y2 = y
	K,p=params
	return [-(y1**2)-np.sin(y2)+p,K*(y1)-(1/y1)*np.cos(y2)]
t = np.linspace(0,10,300)
y0 = [1, 1]
npp = 3 #zadaem p=promezutku [0 do 1 ] c kolichestvom kysochkov=nk
nk = 3
p0=0.1
K0=2
p = np.linspace(0,10,npp)
fig = plt.figure(facecolor='white')
for j in  range(7):
	y0=[1,-pi+(pi/4*j)]
	ys=[0,pi/2]
	ys1=[-pi,-pi/2]
	params=[K0,p0]
	sol=odeint(f, y0, t,args=(params,), full_output=False)
	sol1 = odeint(f, ys, t, args=(params,), full_output=False)
	sol2 = odeint(f, ys1, t, args=(params,), full_output=False)
	#plt.plot(sol[:, 1]%(2*(np.pi)), sol[:, 0],'ro')
	plt.plot(sol1[:, 1], sol1[:, 0])
	#plt.plot(sol2[:, 0])
	plt.xlabel('theta')
	plt.ylabel('vel')
plt.grid(True)
plt.xlim(-5,10)
plt.show()

