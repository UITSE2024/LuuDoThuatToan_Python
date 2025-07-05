n = int(input())

s = 0
t = 1
i = 1

while i <= n:
    t = t * i
    s = (s + t) ** (1 / (i + 1))
    i = i + 1

print(s)
