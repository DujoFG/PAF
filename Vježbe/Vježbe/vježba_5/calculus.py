import numpy as np

class Calculus:
    def __init__(self,f):
        self.f=f

    def d_tocka(self,P,m=None):
        h=0.001
        x=P[0]
        y=P[1]
        if m is None:
            df=(self.f(x+h)-self.f(x-h))/(2*h)
        else:
            df=(self.f(x+h)-y)/h
        print(df)
        return df
    
    def d_int(self,dg,gg,h,m=None):
        točke=[]
        df_t=[]
        for x in np.linspace(dg,gg,20):
            if m is None:
                df=(self.f(x+h)-self.f(x-h))/(2*h)
                točke.append(x)
                df_t.append(df)
            else:
                df=(self.f(x+h)-self.f(x))/h
                točke.append(x)
                df_t.append(df)
        print(točke,df_t)
        return točke,df_t




