n = int(input())
flag = 1
t = n
while(t > 1):
    du = t%5
    if(du):
        flag = 0
    t/=5
if(flag):
    print("la dang")
else:
    print("Khong la dang")