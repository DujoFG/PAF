import particle as prt
import math as m
import numpy as np
import matplotlib.pyplot as plt

p=prt.Particle(10,60,[0,0])
Dan=(100*m.sin(2*p.fi))/9.81
rp=[]
for dt in np.linspace(0.0001,0.1,1000):
    rp.append((abs(Dan-p.range(dt))*100)/Dan)
    p.reset()

plt.plot(np.linspace(0.0001,0.1,1000),rp)
plt.xlabel("dt/[s]")
plt.ylabel("Relativna pogreška/[%]")
plt.show()