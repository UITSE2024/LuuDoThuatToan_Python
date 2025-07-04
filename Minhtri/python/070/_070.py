from re import X


n=int(input("Nhap n: "))
s=0
t=1
i=2
while (i<=2*n):
    t=t*x*x
    s+=t
    i+=2
print("ket qua: ",s)