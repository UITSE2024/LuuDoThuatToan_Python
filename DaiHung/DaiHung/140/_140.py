a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))

delta = b * b - 4 * a * c

if delta > 0:
    x1 = (-b + delta ** 0.5) / (2 * a)
    x2 = (-b - delta ** 0.5) / (2 * a)
    print(f"Phuong trinh co 2 nghiem phan biet: x1 = {x1}, x2 = {x2}")
elif delta == 0:
    x = -b / (2 * a)
    print(f"Phuong trinh co nghiem kep: x = {x}")
else:
    print(f"Phuong trinh vo nghiem")
