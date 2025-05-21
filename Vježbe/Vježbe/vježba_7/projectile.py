import math as m
import numpy as np 
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self,fi0,v0,r0,ro,Cd,A,m0):
        self.fi0=m.radians(fi0)
        self.v0=v0
        self.r0=r0
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

    def reset(self): 
        self.vx=[self.v0*m.cos(self.fi0)]
        self.vy=[self.v0*m.sin(self.fi0)]
        self.x=[self.r0[0]]
        self.y=[self.r0[1]]
        self.ax=[0]
        self.ay=[-9.81]
        self.t=[0]
    
    def kosi_hitac(self,dt):
        self.reset()
        i=0
        t=dt
        while self.y[i]>=0:
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
    
    def ax(self,vx):
        return -np.sign(vx)*((self.ro*self.Cd*self.A)/(2*self.m0))*(vx)**2
    
    def ay(self,vy):
        return -9.81-np.sign(vy)*((self.ro*self.Cd*self.A)/(2*self.m0))*(vy)**2

    def Runge_Kutta(self,dt):
        self.reset()
        i=0
        t=dt
        while self.y[i]>=0:
            k1vx=self.ax(self.vx[i])*dt
            k1x=self.vx[i]*dt
            k2vx=self.ax(self.vx[i]+(k1vx/2))*dt
            k2x=(self.vx[i]+(k1vx/2))*dt
            k3vx=self.ax(self.vx[i]+(k2vx/2))*dt
            k3x=(self.vx[i]+(k2vx/2))*dt
            k4vx=self.ax(self.vx[i]+k3vx)*dt
            k4x=(self.vx[i]+k3vx)*dt
            self.vx.append(self.vx[i]+(1/6)*(k1vx+2*k2vx+2*k3vx+k4vx))
            self.x.append(self.x[i]+(1/6)*(k1x+2*k2x+2*k3x+k4x))
            k1vy=self.ay(self.vy[i])*dt
            k1y=self.vy[i]*dt
            k2vy=self.ay(self.vy[i]+(k1vy/2))*dt
            k2y=(self.vy[i]+(k1vy/2))*dt
            k3vy=self.ay(self.vy[i]+(k2vy/2))*dt
            k3y=(self.vy[i]+(k2vy/2))*dt
            k4vy=self.ay(self.vy[i]+k3vy)*dt
            k4y=(self.vy[i]+k3vy)*dt
            self.vy.append(self.vy[i]+(1/6)*(k1vy+2*k2vy+2*k3vy+k4vy))
            self.y.append(self.y[i]+(1/6)*(k1y+2*k2y+2*k3y+k4y))
            self.t.append(t)
            t+=dt
            i+=1
        return self.x,self.vx,self.y,self.vy,self.t


p=Projectile(45,10,[0,0],1.225,1.05,1,1)
x,vx,y,vy,t=p.Runge_Kutta(0.01)
plt.plot(x,y,color="red")
x,vx,ax,y,vy,ay,t=p.kosi_hitac(0.001)
plt.plot(x,y)
plt.show()
