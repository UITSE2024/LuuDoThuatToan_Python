
from math import sqrt

xA = float(input("Nhap xA: "))
yA = float(input("Nhap yA: "))
xB = float(input("Nhap xB: "))
yB = float(input("Nhap yB: "))
xC = float(input("Nhap xC: "))
yC = float(input("Nhap yC: "))

a = sqrt((xB-xA)**2 + (yB-yA)**2)
b = sqrt((xC-xA)**2 + (yC-yA)**2)
c = sqrt((xC-xB)**2 + (yC-yB)**2)

if(a+b>c and a+c>b and b+c>a):
    print("La tam giac")
else: 
    print("Khong la tam giac")