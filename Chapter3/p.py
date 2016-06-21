
from pylab import *
import math



def reduce_theta(x):
    if abs(x)>math.pi:
        return reduce_theta(x-sign(x)*2*math.pi)
    else:
	return x

#Calculation for w & theta on the p-surface
omega = 0
g = 9.8
l = 9.8
q = 0.5
dt = 0.04
F = 1.0
Omega_D = 2.0/3.0
theta = 0.2
t = 0
k = 0
o_array = []
t_array = []
i=0
while i<500000:
	if abs(t-(2*k*math.pi+math.pi/4)/Omega_D)<0.02:
		o_array.append(omega)
		t_array.append(theta)
		k += 1
	
	omega = omega + (-g/l*math.sin(theta)-q*omega + F*math.sin(Omega_D*t))*dt
	theta += omega*dt
	theta = reduce_theta(theta)
	t += dt
	i += 1
	
scatter(t_array,o_array,color='g', s=1)
text(2.5,1,'$\pi$/4 out-of-phase',color='black',ha='center',fontsize=20)
xlabel('$ theta (rad)$')
ylabel('$\omega (rad/s)$')
savefig('p-surface1.0.png')
show()
