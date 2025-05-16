import math as m

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
        print(len(self.x),len(self.t))
        return [self.t,self.x,self.v,self.a]

    def period(self):
        br=0
        while br<=2:
            for i in range(1,len(self.x)):
                if self.x[i-1]*self.x[i]<0:
                    br+=1
                if br==1:
                    t1=self.t[i]
                if br==2:
                    t2=self.t[i]
                    
        T=2*(t2-t1)
        return T


            



      
