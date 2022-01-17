import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy.linalg as lin
from tkinter.ttk import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
from tkinter import *

def clicked():
	# 'Гравитационное влияние Луны', 'Гравитационное влияние Солнца', 'Океанские приливы', 'Солнечное давление'])  # , 5e-6, 2e-6, 5e-10, 1e-7
	x = Combox.get()
	if "Земли" in x:
		vozm = 5e-5
	elif "Луны" in x:
		vozm = 5e-6
	elif "Солнца" in x:
		vozm = 2e-6
	elif "Океанские" in x:
		vozm = 5e-10
	elif "давление" in x:
		vozm = 1e-7
	else:
		return 0
	# try:
	# 	Amplituda = int(txt_amp.get())
	# 	Period = int(txt_per.get())
	# 	Visota = float(txt_vis.get())
	# except:
	# 	return
	# x = np.linspace(0, 2 * pi, N)
	# print(Amplituda, Period, Visota)
	# print(vozm)
	m=398.6005*(10**12)
	H = 400e3
	Re = 6371*10**3
	r = H+Re
	l = 2*3.14*(r**3/m)**0.5
	r0 = [r, 0,0]
	v0 = (m/lin.norm(r0))**(1/2)
	x0, y0, z0 = r0
	vx0, vy0, vz0, = 0, v0, 0
	F0 = np.array([x0, y0, z0, vx0, vy0, vz0])
	def f(F, t,params):
			x, y, z = F[0], F[1], F[2]
			vx, vy, vz = F[3], F[4], F[5]
			return [vx, vy, vz,-m*x/((lin.norm([x,y,z]))**3),-m*y/((lin.norm([x,y,z]))**3),-m*z/((lin.norm([x,y,z]))**3)]
	def f1(F, t,params):
			x, y, z = F[0], F[1], F[2]
			vx, vy, vz = F[3], F[4], F[5]
			for n in range(10):
				c = (n / np.math.factorial(n)) * np.sin(t)
			return [vx, vy, vz,-m*(x)/((lin.norm([x,y,z]))**3),-m*(y)/((lin.norm([x,y,z]))**3),-m*(z*3*np.sin(1))/((lin.norm([x,y,z]))**3)+c+1+vozm]

	t = np.arange(0,l*5,60)
	psoln = odeint(f, F0, t, args=(m,)).T
	psoln1 = odeint(f1, F0, t, args=(m,)).T
	X, Y, Z = psoln[0], psoln[1], psoln[2]
	# move nevozmushenniy down
	Z -= 8e5
	X1, Y1, Z1 = psoln1[0], psoln1[1], psoln1[2]
		# print(psoln)
		#plt.plot(psoln[:, 0],psoln[:, 1])
		#plt.grid(True)
		#plt.show()
	ax=plt.figure().add_subplot(111,projection="3d")
	ax.set_xlabel("x")
	ax.set_ylabel("y")
	ax.set_zlabel("z")
	ax.set_xlim(-8e6, 8e6)
	ax.set_ylim(-8e6, 8e6)
	ax.set_zlim(-8e6, 8e6)
		# xxx=np.arange(-8e5, 8e5, 1e3)
		# yyy=np.arange(-8e5, 8e5, 1e3)
		# zzz=np.arange(-8e5, 8e5, 1e3)
		# xxx, yyy, zzz = np.meshgrid(xxx, yyy, zzz)
	ax.plot(X, Y, Z, color='blue')
	ax.plot(X1, Y1, Z1, color='red')
	plt.show()

root = Tk()
root.configure(bg='#E8ADAA')
root.title("Space orbit")
root.geometry("370x300")
Combox=Combobox(root, values=['Полярное сжатие Земли','Гравитационное влияние Луны','Гравитационное влияние Солнца','Океанские приливы','Солнечное давление'], width=30)		#5e-5, 5e-6, 2e-6, 5e-10, 1e-7
Combox.current(0)
Combox.place(x=100, y=100)
btn = Button(root, text = "Run!", command = clicked)#, bg = "#F778A1")
btn.place(x=150, y=200)
root.mainloop()