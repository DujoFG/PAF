class HarmonicOscillator:
    def __init__(self):
        self.t=[]
        self.a=[]
        self.v=[]
        self.x=[]

    def oscilator(self,x0,v0,k,m,dt,T):
        t=0
        i=0
        self.x=[x0]
        self.v=[v0]
        while t<=T:
            self.a[i]=-(k/m)*self.x[i]
            self.v[i+1]=self.v[i]+self.a[i]*dt
            self.x[i+1]=self.x[i]+self.v[i]*dt
            self.a.append(self.a[i])
            self.v.append(self.v[i+1])
            self.x.append(self.x[i+1])
            self.t.append(t)
            t+=dt
            i+=1
        print(self.x,self.v,self.a)
        return self.x,self.v,self.a

c=HarmonicOscillator()
c.oscilator(0.3,0,10,0.1,0.1,2)


            



      
