import math as m
import matplotlib.pyplot as plt

M = [0.052, 0.124, 0.168, 0.236, 0.284, 0.336]
fi = [0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472]

u=[]
kfi=[]
kM=[]
for i,el in enumerate(M):
    mfi=el*fi[i]
    u.append(mfi)
    fik=(fi[i])**2
    kfi.append(fik)
    Mk=el**2
    kM.append(Mk)

br=sum(u)/(len(u))
nz=sum(kfi)/(len(kfi))
dt=br/nz
sigma=m.sqrt((1/(len(M)))*(((sum(kM)/len(M))/(nz))-dt**2))
plt.plot(fi,[dt*j for j in fi])
plt.plot(fi,[(dt+sigma)*j for j in fi],color="red",linestyle='--',linewidth=0.5)
plt.plot(fi,[(dt-sigma)*j for j in fi],color="black",linestyle='--',linewidth=0.5)
plt.scatter(fi,M)
plt.xlabel("fi/[rad]")
plt.ylabel("M/[Nm]")
plt.show()