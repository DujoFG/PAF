import math as m
import numpy as np 
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self,fi0,v0,r0,ro,Cd,A,m0):
        self.fi0=m.radians(fi0)
        self.vx=[v0*m.cos(self.fi0)]
        self.vy=[v0*m.sin(self.fi0)]
        self.x=[r0[0]]
        self.y=[r0[1]]
        self.ax=[0]
        self.ay=[-9.81]
        self.t=[0]
        self.ro=ro
        self.Cd=Cd
        self.A=A
        self.m0=m0
    
    def kosi_hitac(self,dt):
        i=0
        t=dt
        while self.y[i]>=0:
            fi=m.atan(abs(self.vy[i]/self.vx[i]))
            self.ax.append(-np.sign(self.vx[i])*((self.ro*self.Cd*self.A)/(2*self.m0))*(self.vx[i])**2)
            self.vx.append(self.vx[i]+self.ax[i]*dt)
            self.x.append(self.x[i]+self.vx[i+1]*dt)
            self.ay.append(-9.81-np.sign(self.vy[i])*((self.ro*self.Cd*self.A)/(2*self.m0))*(self.vy[i])**2)
            self.vy.append(self.vy[i]+self.ay[i]*dt)
            self.y.append(self.y[i]+self.vy[i+1]*dt)  
            self.t.append(t)
            t+=dt
            i+=1
        return self.x,self.vx,self.ax,self.y,self.vy,self.ay,self.t
        
p=Projectile(45,10,[0,0],1.225,1.05,1,1)
x,vx,ax,y,vy,ay,t=p.kosi_hitac(0.001)
print(ax)
print(vx)
plt.plot(x,y)
plt.show()
