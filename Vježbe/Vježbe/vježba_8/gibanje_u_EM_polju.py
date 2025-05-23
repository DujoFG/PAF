import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Gibanje_u_EM_polju:
    def __init__(self,r0,v0,E,B,m0,q): #x0,v0,E,B su vektori i pišu se (x,y,z)
        self.r0=r0
        self.v0=v0
        self.v=[np.array(self.v0)]
        self.a=[np.array((0,0,0))]
        self.r=[np.array(self.r0)]
        self.E=np.array(E)
        self.B=np.array(B)
        self.m0=m0
        self.q=q
        self.t=[0]

    def reset(self):
        self.v=[np.array(self.v0)]
        self.a=[np.array((0,0,0))]
        self.r=[np.array(self.r0)]
        self.t=[0]

    def gibanje(self,dt,T):
        N=int(T/dt)
        t=dt
        for i in range(0,N+1):
            self.a.append((self.q/self.m0)*(self.E+np.cross(self.v[i],self.B)))
            self.v.append(self.v[i]+self.a[i]*dt)
            self.r.append(self.r[i]+self.v[i+1]*dt)
            self.t.append(t)
            t+=dt
        return self.a,self.v,self.r,self.t


g=Gibanje_u_EM_polju((0,0,0),(0.1,0.1,0.1),(0,0,0),(0,0,1),1,-1)
a,v,r,t=g.gibanje(0.01,20)
x=[p[0] for p in r]
y=[p[1] for p in r]
z=[p[2] for p in r]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()

        