x1=(input("Unesite x1:"))
y1=(input("Unesite y1:"))
x2=(input("Unesite x2:"))
y2=(input("Unesite y2:"))

while x1 not in "0123456789":
    print("Krivi unos")
    x1=(input("Unesite x1:"))
while y1 not in "0123456789":
    print("Krivi unos")
    y1=(input("Unesite y1:"))
while x2 not in "0123456789":
    print("Krivi unos")
    x2=(input("Unesite x2:"))
while y2 not in "0123456789":
    print("Krivi unos")
    y2=(input("Unesite y2:"))
    print(x1,x2,y1,y2)
    
x1=float(x1)
y1=float(y1)
x2=float(x2)
y2=float(y2)
k=((y2-y1)/(x2-x1))
l=k*x1+y1
if l>=0:
    pzl="+"
else:
    pzl="-"
print("y={}x{}{}".format(k,pzl,l))
