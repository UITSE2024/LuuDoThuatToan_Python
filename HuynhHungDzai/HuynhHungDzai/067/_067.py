n = int(input("Nhap vao gia tri n: "))

flag = 0
t = n

while(t != 0):
    dv = t %10
    if(dv % 2 != 0):
        flag = 1
    t /= 10

if(flag): 
    print("TT")
else:
    print("Ko TT")




