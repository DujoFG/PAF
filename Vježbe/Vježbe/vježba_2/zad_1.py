import numpy as np
import matplotlib.pyplot as plt

F=float(input('Unesite iznos sile u N:'))
m=float(input('Unesite iznos mase u kg:'))
dt=0.5
t=np.arange(0,10+dt,dt)
a0=F/m
v0=0
s0=0
a_t=[a0]
v_t=[v0]
s_t=[s0]
for i,time in enumerate(t):
    if i>0:
        a_t.append(a0)
        v_t.append(v_t[i-1]+a_t[i]*dt)
        s_t.append(s_t[i-1]+v_t[i]*dt)

plt.subplot(1,3,1)
plt.xlabel('t/[s]')
plt.ylabel('s(t)/[m]')
plt.scatter(t,s_t)

plt.subplot(1,3,2)
plt.xlabel('t/[s]')
plt.ylabel('v(t)/[m/s]')
plt.scatter(t,v_t)

plt.subplot(1,3,3)
plt.xlabel('t/[s]')
plt.ylabel('a(t)/[m/s^2]')
plt.scatter(t,a_t)
plt.tight_layout()
plt.show()
