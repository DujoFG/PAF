import math as m
import numpy as np

def ars_stdv(toč):
    br=0
    brsd=0
    for i in toč:
        br+=i
    ars=br/len(toč)
    for i in toč:
        brsd+=(i-ars)**2
    stdv=m.sqrt(brsd/(len(toč)*(len(toč)-1)))
    print("{}+-{}".format(ars,stdv))
    
toč=[2,3,4,1,5,3,2,4,4,1]   
ars_stdv(toč)

def ars_stdv_mod(toč):
    np.polyfit()
