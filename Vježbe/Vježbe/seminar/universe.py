import numpy as np
import matplotlib.pyplot as plt

class Planet:
    def __init__(self,Mp,r0,v0): #r0=[x0,y0], v0=[vx0,vy0]
        self.Mp=Mp
        self.r0=np.array(r0)
        self.v0=np.array(v0)

    def podaci(self):
        return self.r0, self.v0, self.Mp

    def sila_na_Planet(self,rp1,r_dp,m_dp):
        Fuk=0
        G=6.67*10**(-11)
        for n, rp2 in enumerate(r_dp):
            if not np.array_equal(rp1, rp2):
                udaljenost=np.sqrt((rp1[0]-rp2[0])**2+(rp1[1]-rp2[1])**2)
                smjersile=(rp2-rp1)/udaljenost
                Fuk+=((G*self.Mp*m_dp[n])/udaljenost**2)*smjersile
        return Fuk
    
    def pomak(self,rp1,vp1,r_dp,m_dp,dt):
        a=self.sila_na_Planet(rp1,r_dp,m_dp)/self.Mp
        v=vp1+a*dt
        r=rp1+v*dt
        return r,v,a
  
class Universe:
    def __init__(self,Sunce,Merkur,Venera,Zemlja,Mars):#Sunce=Mp,[x,y],[vx,vy]
        self.Sunce=Planet(*Sunce)
        self.Merkur=Planet(*Merkur)
        self.Venera=Planet(*Venera)
        self.Zemlja=Planet(*Zemlja)
        self.Mars=Planet(*Mars)

    def početni_podaci(self):
        rs,vs,ms=self.Sunce.podaci()
        rm,vm,mm=self.Merkur.podaci()
        rv,vv,mv=self.Venera.podaci()
        rz,vz,mz=self.Zemlja.podaci()
        rM,vM,mM=self.Mars.podaci()
        r0_p=[rs,rm,rv,rz,rM]
        v0_p=[vs,vm,vv,vz,vM]
        m_p=[ms,mm,mv,mz,mM]
        return r0_p,v0_p,m_p
    
    def gibanje(self,dt,T):
        r0_p,v0_p,m_p=self.početni_podaci()
        rg=[]
        vg=[]
        ag=[]
        tt=[]
        r_p=[r0_p]
        v_p=[v0_p]
        i=0
        t=0
        while t<=T:
            rS,vS,aS=self.Sunce.pomak(r_p[i][0],v_p[i][0],r_p[i],m_p,dt)
            rm,vm,am=self.Merkur.pomak(r_p[i][1],v_p[i][1],r_p[i],m_p,dt)
            rV,vV,aV=self.Venera.pomak(r_p[i][2],v_p[i][2],r_p[i],m_p,dt)
            rZ,vZ,aZ=self.Zemlja.pomak(r_p[i][3],v_p[i][3],r_p[i],m_p,dt)
            rM,vM,aM=self.Mars.pomak(r_p[i][4],v_p[i][4],r_p[i],m_p,dt)
            rg.append([rS,rm,rV,rZ,rM])
            vg.append([vS,vm,vV,vZ,vM])
            ag.append([aS,am,aV,aZ,aM])
            v_p.append([vS,vm,vV,vZ,vM])
            r_p.append([rS,rm,rV,rZ,rM])
            tt.append(t)
            i+=1
            t+=dt
        return rg,vg,ag,tt

    def putanja(self,dt,T):#T u godinama,dt u sekundama
        Tp=T*365*24*3600
        rg,vg,ag,tt=self.gibanje(dt,Tp)
        rs=[]
        rm=[]
        rv=[]
        rz=[]
        rM=[]
        for r in rg:
            rs.append(r[0])
            rm.append(r[1])
            rv.append(r[2])
            rz.append(r[3])
            rM.append(r[4])

            plt.plot([r[0] for r in rs],[r[1] for r in rs],color="yellow",label="Sunce")
            plt.plot([r[0] for r in rm],[r[1] for r in rm],color="purple",label="Merkur")
            plt.plot([r[0] for r in rv],[r[1] for r in rv],color="green",label="Venera")
            plt.plot([r[0] for r in rz],[r[1] for r in rz],color="blue",label="Zemlja")
            plt.plot([r[0] for r in rM],[r[1] for r in rM],color="red",label="Mars")
            plt.pause(0.0001)
        plt.show()
    
    def položaj(self,dt,T):
        Tp=T*365*24*3600
        rg,vg,ag,tt=self.gibanje(dt,Tp)
        rs=[]
        rm=[]
        rv=[]
        rz=[]
        rM=[]
        for r in rg:
            rs.append(r[0])
            rm.append(r[1])
            rv.append(r[2])
            rz.append(r[3])
            rM.append(r[4])

        plt.scatter(rs[-1][0],rs[-1][1],color="yellow",label="Sunce",s=5)
        plt.scatter(rm[-1][0],rm[-1][1],color="purple",label="Merkur",s=5)
        plt.scatter(rv[-1][0],rv[-1][1],color="green",label="Venera",s=5)
        plt.scatter(rz[-1][0],rz[-1][1],color="blue",label="Zemlja",s=5)
        plt.scatter(rM[-1][0],rM[-1][1],color="red",label="Mars",s=5)
        plt.show()

        
U=Universe([1.989e30,[0,0],[0,0]],[3.285e23,[57.91e9,0],[0,47.9e3]],[4.867e24,[108.2e9,0],[0,35.2e3]],[6e24,[149.6e9,0],[0,29.8e3]],[6.4191e23,[228e9,0],[0,24.077e3]])
U.putanja(115200,1)