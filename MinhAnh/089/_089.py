x=int(input("Nhap x: "))
n=int(input("Nhap n: "))
s=0
t=1
m=0
i=1
dau=-1
while i<= n:
    t *= x
    m += i
    s += dau*t/m
    dau *= -1
    i += 1
print(s)
