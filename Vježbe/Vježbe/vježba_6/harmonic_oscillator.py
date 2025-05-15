import matplotlib.pyplot as plt
import numpy as np

class HarmonicOscillator:
    def __init__(self, x0, v0 , m, k, dt, T):
        self.m = m
        self.k = k
        self.x0 = x0
        self.v0 = v0
        self.dt = dt
        self.T = T
        self.omega = np.sqrt(k / m)
        self.N = int(T / dt)
        self.t = np.linspace(0, T, self.N)
        self.te=[]
        self.a=[]
        self.v=[]
        self.x=[]

    def oscilator(self):
        t=1
        i=0
        self.x=[self.x0]
        self.v=[self.v0]
        self.a=[-(self.k/self.m)*self.x[0]]
        self.te=[0]
        while t<=self.T:
            self.v.append(self.v[i]+self.a[i]*self.dt)
            self.x.append(self.x[i]+self.v[i]*self.dt)
            self.a.append(-(self.k/self.m)*self.x[i])
            self.te.append(t)
            t+=self.dt
            i+=1
        return [self.te,self.x,self.v,self.a]
    
    def analytical_solution(self):
        self.omega = np.sqrt(self.k / self.m)
        x = self.x0 * np.cos(self.omega * self.t) + (self.v0 / self.omega) * np.sin(self.omega * self.t)
        v = -self.x0 * self.omega * np.sin(self.omega * self.t) + self.v0 * np.cos(self.omega * self.t)
        a = -self.omega**2 * x
        return [self.t,x, v, a]


c=HarmonicOscillator(0.3,0,1,1,0.01,20)
h=c.oscilator()
an=c.analytical_solution()
plt.plot(h[0],h[1],color="red")
plt.scatter(an[0],an[1])
plt.show()
plt.plot(h[0],h[2],color="green")
plt.scatter(an[0],an[2])
plt.show()
plt.plot(h[0],h[3],color="black")
plt.scatter(an[0],an[3])
plt.show()
            



      
