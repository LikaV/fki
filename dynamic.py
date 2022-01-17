from numpy import*
from scipy import optimize
import time
ti = time.clock()
n=100
def f(x):
         f = zeros([n])
         for i in arange(0,n-1,1):
             for R in range(0,1,10):
                 for ksi in range(0,1,10):
                     f[i] = -2*(R^2)*(x[i]^4)-(x[i]^3)*(20,6*(R^2)-(ksi^2)*20,2)-(x[i+1]^2)*(19,84*(R^2)-4*(ksi^2)-0,76*(R^2))-0,8008*ksi
                 f [0] = -2*(R^2)*(x[0]^4)-(x[0]^3)*(20,6*(R^2)-(ksi^2)*20,2)-(x[0]^2)*(19,84*(R^2)-4*(ksi^2)-0,76*(R^2))-0,8008*ksi
                 f[n-1] = -2*(R^2)*(x[n-1]^4)-(x[n-1]^3)*(20,6*(R^2)-(ksi^2)*20,2)-(x[n-2]^2)*(19,84*(R^2)-4*(ksi^2)-0,76*(R^2))-0,8008*ksi
                 return f
x0 =zeros([n])
sol = optimize.root(f, [0, 0], method='hybr')
print('Solution:\n', sol.x)

