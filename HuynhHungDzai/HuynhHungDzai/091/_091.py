n = int(input("Nhap vao n: "))
x = float(input("Nhap vao x: "))

s = -1
t = 1
m = 1
dau = 1

for i in range(2, 2*n + 1, 2):
    t *= x * x
    m *= i*(i - 1)
    s += dau * t/m
    dau = -dau

print("Gia tri cua s: {:.2f}".format(s))




