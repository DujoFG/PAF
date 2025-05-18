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
            fi=m.atan(self.vy[i]/self.vx[i])
            self.x.append(self.x[i]+self.vx[i]*dt)
            self.vx.append(self.vx[i]+self.ax[i]*dt)
            self.ax.append(-np.sign(self.vx[i])*((self.ro*self.Cd*self.A*m.sin(fi))/(2*self.m0))*(self.vx[i])**2)
            self.y.append(self.y[i]+self.vy[i]*dt)
            self.vy.append(self.vy[i]+self.ay[i]*dt)
            self.ay.append(-9.81-np.sign(self.vy[i])*((self.ro*self.Cd*self.A*m.cos(fi))/(2*self.m0))*(self.vy[i])**2)
            self.t.append(t)
            t+=dt
            i+=1
        print(self.x,self.y)
        return [[self.x,self.vx,self.ax],[self.y,self.vy,self.ay],[self.t]]
        
p=Projectile(45,100,[0,0],1.225,1.05,1,1)
p.kosi_hitac(0.1)
