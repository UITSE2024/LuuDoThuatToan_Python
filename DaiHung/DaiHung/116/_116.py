n = int(input("Nhap n: "))

att = 1
at = 2
i = 2

while i <= n:
    ahh = 4 * at + att
    i = i + 1
    att = at
    at = ahh

print("a(n) =", ahh)
   
