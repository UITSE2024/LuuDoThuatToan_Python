n = int(input("Nhap n: "))

s = 0

for i in range(1, 2*n + 2, 2):
    s += 1/i

print("Gia tri cua s: {:.2f}".format(s))



