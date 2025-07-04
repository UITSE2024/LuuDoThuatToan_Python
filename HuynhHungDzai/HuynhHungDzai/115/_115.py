n = int(input("Nhap vao n:"))

att = -1
at = 3

for i in range(2, n + 1):
    ahh = 5 * at + 6*att
    att = at
    at = ahh

print("Gia tri cuoi cung:", at)



