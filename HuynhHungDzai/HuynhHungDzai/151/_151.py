n = int(input("Nhap vao gia tri cua n:"))

flag = 1
t = n

while(t > 1):
    du = t % 2
    if(du != 0):
        flag = 0
    t /= 2

if(flag):
    print("La dang")
else:
    print("Khong la dang")


