import numpy as np

def avg_std(toč):
    avg=np.average(toč)
    std=np.std(toč)
    print("{}+-{}".format(avg,std))

toč=[2,3,4,1,5,3,2,4,4,1] 
avg_std(toč)