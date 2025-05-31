import numpy as np
import matplotlib.pyplot as plt

class Gravitacija:
    def __init__(self, Mz, Ms, v0z, v0s, r0z, r0s): #r0z,r0s=[x0,y0]; v0z,v0s=[v0x,v0y])
        self.v0z=v0z
        self.v0s=v0s
        self.r0z=r0z
        self.r0s=r0s
        self.Ms=Ms  
        self.Mz=Mz
        self.aS=[np.array([0,0])]
        self.aZ=[np.array([0,0])]
        self.vS=[np.array(v0s)]
        self.vZ=[np.array(v0z)]
        self.rS=[np.array(r0s)]
        self.rZ=[np.array(r0z)]
        self.t=[0]
    
    def reset(self):
        self.aS=[np.array([0,0])]
        self.aZ=[np.array([0,0])]
        self.vS=[np.array(self.v0s)]
        self.vZ=[np.array(self.v0z)]
        self.rS=[np.array(self.r0s)]
        self.rZ=[np.array(self.r0z)]
        self.t=[0]
        
    def akc(self,rZ,rS):
        G=6.67408*10**(-11)
        aZ=(-G*self.Ms*(rZ-rS)/np.sqrt((rZ[0]-rS[0])**2+(rZ[1]-rS[1])**2)**3)
        aS=(-G*self.Mz*(rS-rZ)/np.sqrt((rS[0]-rZ[0])**2+(rS[1]-rZ[1])**2)**3)
        return aZ,aS

    def korak(self,dt,T):
        self.reset()
        Ts=T*24*3600
        t=dt
        i=0
        while t<=Ts:
            aZ,aS=self.akc(self.rZ[i],self.rS[i])
            self.aZ.append(aZ)
            self.vZ.append(self.vZ[i]+self.aZ[i]*dt)
            self.rZ.append(self.rZ[i]+self.vZ[i+1]*dt)
            self.aS.append(aS)
            self.vS.append(self.vS[i]+self.aS[i]*dt)
            self.rS.append(self.rS[i]+self.vS[i+1]*dt)
            self.t.append(t)
            i+=1
            t+=dt
        return self.rS,self.rZ
    
G=Gravitacija(5.9742*10**24, 1.989*10**30, [0,29783], [0,0], [1.486*10**11,0], [0,0])
S,Z=G.korak(450,365.24)
xz=[r[0] for r in Z]
yz=[r[1] for r in Z]
xs=[r[0] for r in S]
ys=[r[1] for r in S]
plt.plot(xz,yz,label="Zemlja")
plt.plot(xs,ys,color="yellow",lw=2,label="Sunce")
plt.legend()
plt.show()
