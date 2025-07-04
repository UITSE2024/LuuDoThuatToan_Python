
n = int(input("Nhap n: "))
x = float(input("Nhap x: "))

s = x
t = x
i = 3

while(i<=2*n+1):
    t = t*x*x
    s = s+t
    i = i+2
print(s)
