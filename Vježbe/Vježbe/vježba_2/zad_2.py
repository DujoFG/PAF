import numpy as np
import matplotlib.pyplot as plt
import math 

v0=float(input('Unesite poč. brzinu:'))
fi=float(input('Unesite poč. kut:'))
fi=math.radians(fi)
g=-9.81
dt=0.1
t=np.arange(0,10+dt,dt)
x0=0
y0=0
x_t=[x0]
y_t=[y0]
vy_t=[v0*math.sin(fi)]
for i,time in enumerate(t):
    if i>0:
        vy_t.append(vy_t[i-1]+g*dt)
        x=x_t[i-1]+v0*math.cos(fi)*dt
        if x>=0:
            x_t.append(x)
        else:
            x_t.append(0)
        y=y_t[i-1]+vy_t[i]*dt
        if y>=0:
            y_t.append(y)
        else:
            y_t.append(0)

plt.subplot(1,3,1)
plt.xlabel('x(t)/[m]')
plt.ylabel('y(t)/[m]')
plt.scatter(x_t,y_t)

plt.subplot(1,3,2)
plt.xlabel('t/[s]')
plt.ylabel('y(t)/[m]')
plt.scatter(t,y_t)

plt.subplot(1,3,3)
plt.xlabel('t/[s]')
plt.ylabel('x(t)/[m]')
plt.scatter(t,x_t)
plt.show()
