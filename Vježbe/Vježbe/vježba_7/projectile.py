import math as m

class Projectile:
    def __init__(self,fi0,v0,r0,ro,Cd,A):
        self.fi0=m.radians(fi0)
        self.vx=[v0*m.cos(self.fi0)]
        self.vy=[v0*m.sin(self.fi0)]
        self.x=[r0[0]]
        self.y=[r0[1]]
        self.ax=[0]
        self.ay=[-9.81]
        self.ro=ro
        self.Cd=Cd
        self.A=A
    
    def kosi_hitac(self,dt):
        while self.vy[i]>=0 and self.y[i]>0:
            fi=self.vy[i]/self.vx[i]