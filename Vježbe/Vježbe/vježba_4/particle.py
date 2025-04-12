import math as m
import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self,v0,fi,r0): #r0=[x,y]
        self.x0=r0[0]
        self.y0=r0[1]
        self.r=[r0[0],r0[1]]
        self.fi=m.radians(fi)
        self.vx0=v0*m.cos(self.fi)
        self.vy0=v0*m.sin(self.fi)
        self.v=[v0*m.cos(self.fi),v0*m.sin(self.fi)]
        self.x=[self.r[0]]
        self.y=[self.r[1]]

    def reset(self):
        self.r=[self.x0,self.y0]
        self.v=[self.vx0,self.vy0]
        self.x=[self.r[0]]
        self.y=[self.r[1]]

    def __move(self,dt):
        g=-9.81
        self.r[0]+=self.v[0]*dt
        self.r[1]+=self.v[1]*dt
        self.v[1]+=g*dt
        self.x.append(self.r[0])
        self.y.append(self.r[1])

    def range(self,dt):
        while self.r[1]>=0 or self.v[1]>=0:
            self.__move(dt)
        D=self.r[0]
        self.reset()
        return D
    
    def plot_trajectory(self,dt):
        while self.r[1]>=0 or self.v[1]>=0:
            self.__move(dt)
        plt.plot(self.x,self.y)
        plt.xlabel("x/[m]")
        plt.ylabel("y/[m]")
        plt.axhline(0,c='k')
        plt.show()

