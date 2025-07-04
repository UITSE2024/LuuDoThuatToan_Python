n = int(input("Nhap n: "))

s = 0
i = 1
while (i <= 2*n):
    s = s + 1/(i*(i + 1))
    i = i + 1

print("Tong la: ", s)