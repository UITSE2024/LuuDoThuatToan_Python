
n = int(input("Nhap n: "))

if(n==1):
    ahh=2
else:
    at = 2
    i = 2
    while(i<=n):
        ahh = (at**2 + 2)/(2*at)
        i = i+1
        at=ahh
print(ahh)

