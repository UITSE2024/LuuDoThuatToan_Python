x = float(input())
n = int(input())

s = x + 1.0
t = x
m = 1.0
i = 3

while i <= (2 * n + 1):
    t = t * x ** 2
    m = m * i * (i - 1)
    s = s + t / m
    i = i + 2

print(s)