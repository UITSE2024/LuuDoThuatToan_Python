x = float(input("Nhap x: "))

if (x >= 0):
    if (x <= 1):
        f = 5*x - 7
    else:
        f = 2*x*x*x + 5*x*x - 8*x + 3
else:
    f = -2*x*x*x + 6*x + 9

print("Ket qua: ", f)