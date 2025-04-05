import math as m
def range(v,r,fi,dt):
        g=-9.81
        v=[v*m.cos(m.radians(fi)),v*m.sin(m.radians(fi))]
        x=[r[0]]
        y=[r[1]]
        vy=[v[1]]
        i=0
        while r[1]!=0 or v[1]>=0:
            r[0]=x[i]+v[0]*dt
            x.append(r[0])
            r[1]=y[i]+vy[i]
            y.append(r[1])
            v[1]=vy[i]+g*dt
            vy.append(v[1])
            i+=1
        print(r[0],r[1])
        print(vy)
        print(x)
        print(y)

range(10,[0,0],30,0.1)