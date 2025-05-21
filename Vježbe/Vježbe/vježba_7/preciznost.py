import projectile as pro
import matplotlib.pyplot as plt

p=pro.Projectile(45,10,[0,0],1.225,1.05,1,1)
x,vx,aex,y,vy,aey,t=p.kosi_hitac(0.1)
plt.plot(x,y,color="black",lw=1,label="Euler-0.1s")
plt.xlabel("x/[m]")
plt.ylabel("y/[m]")

x,vx,aex,y,vy,aey,t=p.kosi_hitac(0.01)
plt.plot(x,y,color="blue",lw=1,label="Euler-0.01s")
plt.xlabel("x/[m]")
plt.ylabel("y/[m]")

x,vx,aex,y,vy,aey,t=p.kosi_hitac(0.001)
plt.plot(x,y,color="green",lw=1,label="Euler-0.001s")
plt.xlabel("x/[m]")
plt.ylabel("y/[m]")

x,vx,y,vy,t=p.Runge_Kutta(0.01)
plt.plot(x,y,color="red",lw=1,label="Runge-Kutta-0.01s")
plt.xlabel("x/[m]")
plt.ylabel("y/[m]")

plt.legend()
plt.show()
