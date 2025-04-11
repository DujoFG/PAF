import particle as prt
import numpy as np
import matplotlib.pyplot as plt

p=prt.Particle(10,60,[0,0])
D_t=[]
for dt in np.linspace(0.0001,0.1,1000):
    D_t.append(p.range(dt))

plt.plot(np.linspace(0.0001,0.1,1000),D_t)
plt.xlabel("dt")
plt.ylabel("D(t)")
plt.show()
