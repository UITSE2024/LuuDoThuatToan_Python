n = int(input())

flag = 1
t = n

while t != 0:
    dv = t % 10
    if (dv % 2 != 0):
        flag = 0
    t = t // 10

if flag == 1:
    print("Toan chan")
else:
    print("Khong toan chan")