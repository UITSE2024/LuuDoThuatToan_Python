import math
n = int(input("Nhap n: "))
at = 2
i = 2
while i <= n:
    ahh = 5*at + math.sqrt(24*at*at - 8)
    i = i + 1
print("So hang thu n cua day:", end=" ")
print(ahh)
