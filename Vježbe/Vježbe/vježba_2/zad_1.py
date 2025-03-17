import numpy as np
import matplotlib.pyplot as plt

F=float(input('Unesite iznos sile u N:'))
m=float(input('Unesite iznos mase u kg:'))
x=np.linspace(1,10,10)
a_t=[]
for t in range(1,11):
    a=F/m
    a_t.append(a)
v_t=[]
v=0
for t in range(0,10):
    v+=a*(t-(t-1))
    v_t.append(v)
print(v_t)
plt.plot(x,v_t,'r')
plt.show()
s_t=[]
s=0
for v,t in enumerate(v_t):
    s=s+v*(t-(t-1))
    s_t.append(s)
print(s_t)