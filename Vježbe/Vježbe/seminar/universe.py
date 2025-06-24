import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Planet:
    def __init__(self,Mp,r0,v0,T0,ime): #r0=[x0,y0], v0=[vx0,vy0], ime="Zemlja", T0-dani
        self.Mp=Mp
        self.r0=np.array(r0)
        self.v0=np.array(v0)
        self.r=[self.r0]
        self.v=[self.v0]
        self.a=[]
        self.T0=T0
        self.ime=ime

    def pod_za_gib(self):
        return self.r0, self.v0, self.Mp, self.ime
    
    def Podaci_o_Planetu(self):
        ime="Ime planeta: {}".format(self.ime)
        masa="Masa: {}".format(self.Mp)
        god="Period kruženja: {}".format(self.T0)
        d="Udaljenost od Sunca: {}".format(self.r0)
        brzina="Brzina kruženja: {}".format(self.v0)
        return ime,masa,god,d,brzina

class Universe:
    def __init__(self):
        self.tijela=[]

    def dodaj_tijela(self, *tijela):
        for tijelo in tijela:
            self.tijela.append(tijelo)

    def akceleracija(self):
        G=6.67*10**(-11)
        a_t=[]
        for tijelo in self.tijela:
            auk=0
            for t in self.tijela:
                if t!=tijelo:
                    udaljenost=np.sqrt((tijelo.r[-1][0]-t.r[-1][0])**2+(tijelo.r[-1][1]-t.r[-1][1])**2)
                    smjerakc=(t.r[-1]-tijelo.r[-1])/udaljenost
                    auk+=((G*t.Mp)/udaljenost**2)*smjerakc
            a_t.append(auk)
        return a_t
    
    def pomak(self,dt):
        a_t=self.akceleracija()
        for i,tijelo in enumerate(self.tijela):
            tijelo.a.append(a_t[i])
            tijelo.v.append(tijelo.v[-1]+tijelo.a[-1]*dt)
            tijelo.r.append(tijelo.r[-1]+tijelo.v[-1]*dt)

    def gibanje(self,dt,T):#T u godinama,dt u sekundama
        Tp=T*365*24*3600
        t=0
        while t<=Tp:
            for tijelo in self.tijela:
                self.pomak(dt)
            t+=dt

    def položaj(self,dt,T):
        self.gibanje(dt,T)
        boja=['yellow','grey','orange','blue','red']
        for i,tijelo in enumerate(self.tijela):
            r,v,m,ime=tijelo.pod_za_gib()
            if ime=="Sunce":
                plt.scatter(tijelo.r[-1][0],tijelo.r[-1][1],color=boja[i],label=ime,s=100)
            else:
                plt.scatter(tijelo.r[-1][0],tijelo.r[-1][1],color=boja[i],label=ime,s=20)
        plt.xlabel("x [m]")
        plt.ylabel("y [m]")
        plt.title("Položaj planeta nakon {} godine".format(T))
        plt.legend()
        plt.axis("equal")
        plt.grid(True)
        plt.show()

    def simulacija(self,dt,T):
        self.gibanje(dt, T)
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        ax.set_xlim(-2.5e11, 2.5e11)
        ax.set_ylim(-2.5e11, 2.5e11)

        boje = ['yellow', 'gray', 'orange', 'blue', 'red']
        točke = []

        for i, tijelo in enumerate(self.tijela):
            točka, = ax.plot([], [], 'o', color=boje[i], label=tijelo.ime, markersize=4)
            točke.append(točka)

        def animiraj(frame):
            for j, tijelo in enumerate(self.tijela):
                if frame < len(tijelo.r):
                    točke[j].set_data([tijelo.r[frame][0]], [tijelo.r[frame][1]])
            return točke

        ax.legend()
        for i,tijelo in enumerate(self.tijela):
            r,v,m,ime=tijelo.pod_za_gib()
            linija, =ax.plot([r[0] for r in tijelo.r],[r[1] for r in tijelo.r],ls='--',color=boje[i],lw=1)
            linija.set_dashes([8,12])
        animacija = FuncAnimation(fig, animiraj, frames=range(0,len(self.tijela[0].r),3), interval=0.01, blit=True, repeat=False)
        plt.xlabel("x [m]")
        plt.ylabel("y [m]")
        plt.show()


Sunce=Planet(1.989e30,[0,0],[0,0],0,"Sunce")
Merkur=Planet(3.285e23,[57.91e9,0],[0,47.9e3],120,"Merkur")
Venera=Planet(4.867e24,[108.2e9,0],[0,35.2e3],265,"Venera")
Zemlja=Planet(6e24,[149.6e9,0],[0,29.8e3],365.24,"Zemlja")
Mars=Planet(6.4191e23,[228e9,0],[0,24.077e3],413,"Mars")
Sun_sustav=Universe()
Sun_sustav.dodaj_tijela(Sunce,Merkur,Venera,Zemlja,Mars) 

Sun_sustav.simulacija(14400,1)
