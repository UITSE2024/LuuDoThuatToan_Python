a = float(input("Nhap vao gia tri a:"))
b = float(input("Nhap vao gia tri b:"))

if(a == 0):
    if(b == 0):
        print("VSN")
    else:
        print("VN")
else:
    print("Nghiem: {:.2f}".format(-b/a))



