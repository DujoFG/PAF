
import numpy as np
import matplotlib.pyplot as plt


def pravac():    
    x1=float(input('Unesite x1: '))
    y1=float(input('Unesite y1: '))
    x2=float(input('Unesite x2: '))
    y2=float(input('Unesite y2: '))
    k=((y2-y1)/(x2-x1))
    l=y1-k*x1
    x=np.linspace(x1-1,x2+1)
    y=k*x+(l)

    izb=int(input('PDF(1) ili graf(0): '))
    
    if izb!=0:
        id=input('Unesite ime datoteke:')
        plt.savefig("{}.pdf".format(id), format="pdf")
    else:
        plt.plot(x, y, 'r')
        plt.plot(x1,y1,marker="o")
        plt.plot(x2,y2,marker="o")
        plt.show()
    
pravac()

