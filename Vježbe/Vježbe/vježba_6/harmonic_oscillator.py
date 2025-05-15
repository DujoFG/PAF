import matplotlib.pyplot as plt

class HarmonicOscillator:
    def __init__(self, x0, v0 , m, k, dt, T):
        self.m=m
        self.k=k
        self.x0=x0
        self.v0=v0
        self.dt=dt
        self.T=T
        self.x=[self.x0]
        self.v=[self.v0]
        self.a=[-(k/m)*x0]
        self.t=[0]

    def oscilator(self):
        t=self.dt
        i=0
        while t<=self.T:
            self.v.append(self.v[i]+self.a[i]*self.dt)
            self.x.append(self.x[i]+self.v[i+1]*self.dt)
            self.a.append(-(self.k/self.m)*self.x[i+1])
            self.t.append(t)
            t+=self.dt
            i+=1
        return [self.t,self.x,self.v,self.a]



            



      
