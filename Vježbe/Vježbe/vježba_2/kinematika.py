import numpy as np
import matplotlib.pyplot as plt
import math 

def jednoliko_gibanje(F,m,t,t1,t2,dt):
    t=np.arange(0,t+dt,dt)
    a0=F/m
    v0=0
    s0=0
    i_t=[]
    i_at=[]
    i_vt=[]
    i_st=[]
    a_t=[a0]
    v_t=[v0]
    s_t=[s0]
    for i,time in enumerate(t):
        if i>0:
            a_t.append(a0)
            v_t.append(v_t[i-1]+a_t[i]*dt)
            s_t.append(s_t[i-1]+v_t[i]*dt)
        if time>=t1 and time<=t2:
            i_t.append(time)
            i_at.append(a_t[i])
            i_vt.append(v_t[i])
            i_st.append(s_t[i])

    plt.subplot(1,3,1)
    plt.xlabel('t/[s]')
    plt.ylabel('s(t)/[m]')
    plt.scatter(i_t,i_st)

    plt.subplot(1,3,2)
    plt.xlabel('t/[s]')
    plt.ylabel('v(t)/[m/s]')
    plt.scatter(i_t,i_vt)

    plt.subplot(1,3,3)
    plt.xlabel('t/[s]')
    plt.ylabel('a(t)/[m/s^2]')
    plt.scatter(i_t,i_at)
    plt.tight_layout()
    plt.show()


def kosi_hitac(v0,fi,t,t1,t2,dt):
    fi=math.radians(fi)
    g=-9.81
    t=np.arange(0,t+dt,dt)
    x0=0
    y0=0
    i_t=[]
    i_xt=[]
    i_yt=[]
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
        if time>=t1 and time<=t2:
            i_t.append(time)
            i_xt.append(x_t[i])
            i_yt.append(y_t[i])

    plt.subplot(1,3,1)
    plt.xlabel('x(t)/[m]')
    plt.ylabel('y(t)/[m]')
    plt.scatter(i_xt,i_yt)

    plt.subplot(1,3,2)
    plt.xlabel('t/[s]')
    plt.ylabel('y(t)/[m]')
    plt.scatter(i_t,i_yt)

    plt.subplot(1,3,3)
    plt.xlabel('t/[s]')
    plt.ylabel('x(t)/[m]')
    plt.scatter(i_t,i_xt)
    plt.show()

