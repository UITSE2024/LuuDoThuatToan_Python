n = int(input())

s = 0
m = 0
i = 1
dau = 1

while i <= n:
    m = m + i
    s = s + dau / m
    dau = -dau
    i = i + 1

print(s)