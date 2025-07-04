from math import sqrt
n=int(input("Nhap n: "))
s=0
i=1
while (i<=n):
    s=s+1/((i+1) * (i ** (1/2)) + i * ((i + 1) ** (1/2)))
    i+=1
print("Ket qua: ",s)