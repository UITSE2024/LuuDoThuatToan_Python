n = int(input("Nhap vao n: "))

s = 0
t = 1

for i in range(1, n + 1):
    t *= i
    s += i * t

print("Gia tri cua s:", s)



