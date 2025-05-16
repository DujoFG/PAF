import harmonic_oscillator as ho
import matplotlib.pyplot as plt
import math as m

for dt in [0.01,0.05,0.1]:
    c=ho.HarmonicOscillator(0.3,0,1,10,dt,20)
    h=c.oscilator()

    def analitičko(t,x0,m0,k):
        w=m.sqrt(k/m0)
        return [x0*m.cos(w*t),-w*x0*m.sin(w*t),-w**2*x0*m.cos(w*t)]
    x=[]
    v=[]
    a=[]
    for t in h[0]:
        an=analitičko(t,0.3,1,10)
        x.append(an[0])
        v.append(an[1])
        a.append(an[2])

    plt.plot(h[0],h[1],color="red")
    plt.plot(h[0],x,ls='--')
    plt.xlabel("t/(s)")
    plt.ylabel("x/[m]")
    plt.title("Korak:{}s".format(dt))
    plt.show()
    plt.plot(h[0],h[2],color="green")
    plt.plot(h[0],v,ls='--')
    plt.xlabel("t/(s)")
    plt.ylabel("v/[m/s]")
    plt.title("Korak:{}s".format(dt))
    plt.show()
    plt.plot(h[0],h[3],color="black")
    plt.plot(h[0],a,ls='--')
    plt.xlabel("t/(s)")
    plt.ylabel("a/[m/s**2]")
    plt.title("Korak:{}s".format(dt))
    plt.show()

    print("T numerički:{}".format(c.period()))
    print("T analitički:{}".format((2*m.pi)/(m.sqrt(10))))