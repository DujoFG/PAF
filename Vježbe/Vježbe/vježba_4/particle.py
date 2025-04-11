import math as m
import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self,v,fi,r): #r=[x,y]
        self.fi=m.radians(fi)
        self.r=r
        self.v=[v*m.cos(self.fi),v*m.sin(self.fi)]
        print(self.fi,self.r,self.v)
    
    def reset(self):
       self.v=None
       self.fi=None
       self.r=None
    
    def __move(self,dt):
        self.r[0]=self.r[0]+self.v[0]*dt
        return self.r[0]
    
    def range(self):
        dt=0.0001
        g=-9.81
        x=[self.r[0]]
        y=[self.r[1]]
        vy=[self.v[1]]
        i=0
        while self.r[1]>0 or self.v[1]>=0:
            self.r[0]=x[i]+self.v[0]*dt
            x.append(self.r[0])
            self.r[1]=y[i]+vy[i]*dt
            y.append(self.r[1])
            self.v[1]=vy[i]+g*dt
            vy.append(self.v[1])
            D=x[i]
            i+=1
        print("Domet:",D)

    def plot_trajectory(self,dt):
        g=-9.81
        x=[self.r[0]]
        y=[self.r[1]]
        vy=[self.v[1]]
        i=0
        while self.r[1]>=0 or self.v[1]>=0:
            self.r[0]=x[i]+self.v[0]*dt
            x.append(self.r[0])
            self.r[1]=y[i]+vy[i]*dt
            y.append(self.r[1])
            self.v[1]=vy[i]+g*dt
            vy.append(self.v[1])
            i+=1
        plt.plot(x,y)
        plt.xlabel("x/[m]")
        plt.ylabel("y/[m]")
        plt.axhline(0,c='k')
        plt.show()







        


