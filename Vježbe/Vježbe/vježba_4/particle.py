import math as m

class Particle:
    def __init__(self,v,fi,r):
        self.fi=m.radians(fi)
        self.r=r
        self.v=[v*m.cos(self.fi),v*m.sin(self.fi)]
    
    def reset(self):
       self.v=None
       self.fi=None
       self.r=None
    
    def __move(self,dt):
        self.r[0]=self.r[0]+self.v[0]*dt
        return self.r[0]

    def range(self,dt):
        g=-9.81
        x=[self.r[0]]
        y=[self.r[1]]
        vy=[self.v[1]]
        i=0
        while self.r[1]!=0 or self.v[1]>=0:
            self.r[0]=x[i]+self.v[0]*dt
            x.append(self.r[0])
            self.r[1]=y[i]+vy[i]
            y.append(self.r[1])
            self.v[1]=vy[i]+g*dt
            vy.append(self.v[1])
            D=self.r[0]
            i+=1
        print(D)







        


