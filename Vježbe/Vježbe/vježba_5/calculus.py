import numpy as np

class Calculus:
    def __init__(self,f):
        self.f=f

    def d_tocka(self,P,h,m=None):
        x=P[0]
        y=P[1]
        if m is None:
            df=(self.f(x+h)-self.f(x-h))/(2*h)
        else:
            df=(self.f(x+h)-y)/h
        print(df)
        return df
    
    def d_int(self,dg,gg,h,m=None):
        der=[]
        for x in np.arange(dg,gg,0.2):
            if m is None:
                df=(self.f(x+h)-self.f(x-h))/(2*h)
                der.append([x,df])
            else:
                df=(self.f(x+h)-self.f(x))/h
                der.append([x,df])
        return der

    def int_pr(self,dgi,ggi,N):
        dx=(ggi-dgi)/(N-1)
        Fg=0
        Fd=0
        for x1 in np.linspace(dgi+dx,ggi,N-1):
            Fg+=self.f(x1)*dx
        for x2 in np.linspace(dgi,ggi-dx,N-1):
            Fd+=self.f(x2)*dx
        print(Fg,Fd)
        return [Fg,Fd]

    def int_tr(self,dgi,ggi,N):
        dx=(ggi-dgi)/(N-1)
        F=0
        for x in np.linspace(dgi+dx,ggi,N-1):
            F+=(dx/2)*(self.f(x-dx)+self.f(x))
        print(F)
        return F

def f(x):
    return 2*x+3
c=Calculus(f)
c.int_tr(-1,3,200)