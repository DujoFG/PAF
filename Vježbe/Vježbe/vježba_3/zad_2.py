def zbr_raz(N):
    zbr=0
    raz=5
    for n in range(N):
        zbr+=1/3
        raz-=1/3
    print(zbr)
    print(raz)

zbr_raz(200)
zbr_raz(2000)
zbr_raz(20000)

#Kada prebacivamo 1/3 u binarni oblik ona nema konačan oblik te se kad se to zbroji N puta dobijemo te razlike u nekim decimalam