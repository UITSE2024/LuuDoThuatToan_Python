x = int(input())
y = int(input())
n = x

while n <= y:
    dk1 = ((n % 4 == 0) and (n % 100 != 0))
    dk2 = n % 400 == 0
    if dk1 and dk2:
        print(n)
    n = n + 1
