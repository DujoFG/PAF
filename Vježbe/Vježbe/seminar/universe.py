import numpy as np


class Planet:
    def __init__(self,Mp,r0,v0): #r0=[x0,y0], v0=[vx0,vy0]
        self.Mp=Mp
        self.r0=r0
        self.v0=v0
        self.r=[np.array(r0)]
        self.v=[np.array(v0)]

    def podaci(self):
        return self.r0, self.Mp

    def sila_na_Planet(self,rp1,,mp1,rp2,mp2):
        G=6.67*10**-(11)
        udaljenost=np.sqrt(([0]-rp2[0])**2+(self.r0[1]-rp2[1])**2)
        smjersile=
        return ((G*self.Mp*mp2)/udaljenost**2)