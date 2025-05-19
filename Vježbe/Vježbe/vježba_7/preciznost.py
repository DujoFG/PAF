import projectile as pro
import matplotlib.pyplot as plt

p=pro.Projectile(45,15,[0,0],1,0,1,1)
for dt in [0.1,0.01,0.001]:
    x,vx,ax,y,vy,ay,t=p.kosi_hitac(dt)
    plt.plot(x,y,lw=1)
    plt.xlabel("x/[m]")
    plt.ylabel("y/[m]")
    plt.title("Eulerova metoda")
    plt.show()