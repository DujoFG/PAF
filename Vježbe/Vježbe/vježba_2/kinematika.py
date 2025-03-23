import numpy as np
import matplotlib.pyplot as plt
import math 

def jednoliko_gibanje(F,m,t1,t2,dt):
    t=np.arange(t1,t2+dt,dt)
    a0=F/m
    v0=0
    s0=0
    a_t=[a0]
    v_t=[v0]
    s_t=[s0]
    for i,time in enumerate(t):
        if i>0:
            a_t.append(a0)
            v_t.append(v_t[i-1]+a_t[i]*dt)
            s_t.append(s_t[i-1]+v_t[i]*dt)

    plt.subplot(1,3,1)
    plt.xlabel('t/[s]')
    plt.ylabel('s(t)/[m]')
    plt.scatter(t,s_t)

    plt.subplot(1,3,2)
    plt.xlabel('t/[s]')
    plt.ylabel('v(t)/[m/s]')
    plt.scatter(t,v_t)

    plt.subplot(1,3,3)
    plt.xlabel('t/[s]')
    plt.ylabel('a(t)/[m/s^2]')
    plt.scatter(t,a_t)
    plt.tight_layout()
    plt.show()


def kosi_hitac(v0,fi,t1,t2,dt):
    fi=math.radians(fi)
    g=-9.81
    t=np.arange(t1,t2+dt,dt)
    x0=0
    y0=0
    x_t=[x0]
    y_t=[y0]
    vy_t=[v0*math.sin(fi)]
    for i,time in enumerate(t):
        if i>0:
            vy_t.append(vy_t[i-1]+g*dt)
            x=x_t[i-1]+v0*math.cos(fi)*dt
            if x>=0:
                x_t.append(x)
            else:
                x_t.append(0)
            y=y_t[i-1]+vy_t[i]*dt
            if y>=0:
                y_t.append(y)
            else:
                y_t.append(0)

    plt.subplot(1,3,1)
    plt.xlabel('x(t)/[m]')
    plt.ylabel('y(t)/[m]')
    plt.scatter(x_t,y_t)

    plt.subplot(1,3,2)
    plt.xlabel('t/[s]')
    plt.ylabel('y(t)/[m]')
    plt.scatter(t,y_t)

    plt.subplot(1,3,3)
    plt.xlabel('t/[s]')
    plt.ylabel('x(t)/[m]')
    plt.scatter(t,x_t)
    plt.show()

