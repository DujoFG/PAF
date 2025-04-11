import particle as prt
import math as m
import numpy as np
import matplotlib.pyplot as plt

p=prt.Particle(10,60,[0,0])
Dan=(100*m.sin(120))/9.81
raz=[]
for dt in np.linspace(0.0001,0.1,1000):
    raz.append(Dan-p.range(dt))

plt.plot(np.linspace(0.0001,0.1,1000),raz)
plt.xlabel("dt")
plt.ylabel("raz")
plt.show()
