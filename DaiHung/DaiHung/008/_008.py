import math

n = int(input("Nhap n: "))
r = float(input("Nhap r: "))

p = 2 * n * r * math.sin(math.pi / n)

print(f"Chu vi hinh da giac: {p:.2f}")
