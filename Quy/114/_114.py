n = int(input("Nhap n: "))
if (n == 0):
    ahh = -2
else:
    at = -2
    tt = 3
    pp = 7
    i = 2
    while (i <= n):
        tt = tt * 3
        pp = pp * 7
        ahh = 5*at + 2*tt - 6*pp + 12
        i = i + 1
        at = ahh

print("Ket qua: ", ahh)