n = int(input("Nhap vao n:"))

t = 1
for i in range(1, n + 1, 2):
    if(n % i == 0):
        t *= i 

print("Tich cac uoc le:",t )




