import numpy as np
import matplotlib.pyplot as plt

class Gravitacija:
    def __init__(self, Mz, Ms, v0z, v0s, r0z, r0s): #r0z, r0s=[x0,y0]; v0z,v0s=[v0x,v0y]
        self.Ms=Ms
        self.Mz=Mz
        self.aS=[]
        self.aZ=[]
        self.vS=[v0s]
        self.vZ=[v0z]
        self.rS=[r0s]
        self.rZ=[r0z]
        self.t=[]

    def korak(self,dt,T):
        G=6.67408*10**(-11)
        t=0
        i=0
        while t<=T:
            self.aZ.append((-G*self.Ms*(self.rZ[i]-self.rS[i])/np.sqrt((self.rZ[i])**2-(self.rS[i])**2)**3))
            self.vZ.append(self.vZ[i]+self.aZ[i])
            self.rZ.append(self.rZ[i]+self.vZ[i+1])
            self.aS.append((-G*self.Mz*(self.rS[i]-self.rZ[i])/np.sqrt((self.rS[i])**2-(self.rZ[i])**2)**3))
            self.vS.append(self.vS[i]+self.aS[i])
            self.rS.append(self.rS[i]+self.vS[i+1])
            self.t.append(t)
            i+=1
            t+=dt
        return self.rS,self.rZ
    
G=Gravitacija(5.9742*10**24, 1.989*10**30, [0,29783], [0,0], [1.486*10**11,0], [0,0])
S,Z=G.korak(0.01,365.24)
xz=[r[0] for r in Z]
yz=[r[1] for r in Z]
plt.plot(xz,yz)
plt.show()