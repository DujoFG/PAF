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

    def gibanje_Euler(self,dt,T):
        self.reset()
        N=int(T/dt)
        t=dt
        for i in range(0,N+1):
            self.a.append((self.q/self.m0)*(np.cross(self.v[i],self.B)))
            self.v.append(self.v[i]+self.a[i]*dt)
            self.r.append(self.r[i]+self.v[i+1]*dt)
            self.t.append(t)
            t+=dt
        return self.a,self.v,self.r,self.t

    def aRK(self,v):
        return (self.q/self.m0)*(np.cross(v,self.B))

    def gibanje_RK(self,dt,T):
        self.reset()
        N=int(T/dt)
        t=dt
        for i in range(0,N+1):
            k1v=self.aRK(self.v[i])*dt
            k1r=self.v[i]*dt
            k2v=self.aRK(self.v[i]+(k1v/2))*dt
            k2r=(self.v[i]+(k1v/2))*dt
            k3v=self.aRK(self.v[i]+(k2v/2))*dt
            k3r=(self.v[i]+(k2v/2))*dt
            k4v=self.aRK(self.v[i]+k3v)*dt
            k4r=(self.v[i]+k3v)*dt
            self.v.append(self.v[i]+(1/6)*(k1v+2*k2v+2*k3v+k4v))
            self.r.append(self.r[i]+(1/6)*(k1r+2*k2r+2*k3r+k4r))
            self.t.append(t)
            t+=dt
        return self.r,self.v,self.t

g=Gibanje_u_EM_polju((0,0,0),(0.1,0.1,0.1),(0,0,0),(0,0,1),1,-1)
a,v,r,t=g.gibanje_Euler(0.01,20)
xe=[p[0] for p in r]
ye=[p[1] for p in r]
ze=[p[2] for p in r]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(xe, ye, ze)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

r,v,t=g.gibanje_RK(0.01,20)
xrk=[p[0] for p in r]
yrk=[p[1] for p in r]
zrk=[p[2] for p in r]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(xrk, yrk, zrk)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()

        