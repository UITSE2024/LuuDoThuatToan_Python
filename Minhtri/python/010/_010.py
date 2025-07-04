from math import sqrt
x1=int(input("Nhap x1: "))
y1=int(input("Nhap y1: "))
x2=int(input("Nhap x2: "))
y2=int(input("Nhap y2: "))
x3=int(input("Nhap x3: "))
y3=int(input("Nhap y3: "))
a=sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
b=sqrt((x3-x2)*(x3-x2)+(y3-y2)*(y3-y2))
a=sqrt((x3-x1)*(x3-x1)+(y3-y1)*(y3-y1))
p=a+b+c
print("Chu vi: ",p)