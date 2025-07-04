from math import sin
x=int(input("Nhap x: "))
n=int(input("Nhap n: "))
s=0
t=1
i=1
while (i<=n):
    t=t*sin(x)
    s+=t
    i+=i
print("Ket qua: ",s)