import math as m

def ars_stdv(toč):
    br=0
    brsd=0
    for i in toč:
        br+=i
    ars=br/len(toč)
    for i in toč:
        brsd+=(i-ars)**2
    stdv=m.sqrt(brsd/(len(toč)))
    print("{}+/-{}".format(ars,stdv))
    
toč=[2,3,4,1,5,3,2,4,4,1]   
ars_stdv(toč)


