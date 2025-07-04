from math import sqrt

n = int(input("Nhap n: "))

s = 0
i = n
while(i>0):
    s = s + sqrt(i+s)
    i = i-1
print(s)


