
from pylab import *
import math

theta=[]
w=[]
t=[]


#1. initial parameter
#Dimensionalize the equatin
g=9.8 #local gravitational acceleration of Earth(m*s^(-2))
l=9.8

theta0=0.2
theta.append(theta0)
w_0 = 0
w.append(w_0)
t.append(0.0)

T = float(input('Total time = '))
dt = float(input('dt = '))

F = float(input('F_D='))
Omega_D = float(input('Omega_D ='))
q = float(input('q=2 beta='))


#2. calculation
n=int(T/dt)
for i in range(1,n+1):
    w.append(w[-1]-(9.8*math.sin(theta[-1])/l+q*w[-1]-F*math.sin(Omega_D*t[-1]))*dt)
    tmp=theta[-1]+w[-1]*dt
    if abs(tmp)>math.pi:
        tmp=tmp-sign(tmp)*2*math.pi
    theta.append(tmp)
    t.append(t[-1]+dt)
    print t[-1],theta[-1],w[-1]

#3. plot
plot(t,theta,'g')
title('Nonlinear Pendulum ',fontsize=20)
xlabel('t(s)')
ylabel('$theta (rad)$')
savefig('theta-t.png')
show()

scatter(theta,w,color='g',s=1)
title('phase diagram',fontsize=20)
xlabel('$ theta (rad)$')
ylabel('$\omega (rad/s)$')
savefig('phase diagram.png')
show()
