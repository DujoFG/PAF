class Calculus:
    def __init__(self,f):
        self.f=f

    def derivacija(self,P,m=None):
        h=0.001
        x=P[0]
        y=P[1]
        if m is None:
            df=(self.f(x+h)-self.f(x-h))/(2*h)
        else:
            df=(self.f(x+h)-y)/h
            print("2")
        print(df)
        return df
    

def f(x):
    return 2*x-3
c=Calculus(f)
c.derivacija([0,-3],1)


