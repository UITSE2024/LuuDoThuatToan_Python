n = int(input("Nhap vao n: "))

s = 0
for i in range (1, n + 1):
    s += 1/(i * (i + 1) * (i + 2))

print("Gia tri cua {:.2f}".format(s))




