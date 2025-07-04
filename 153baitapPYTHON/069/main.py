n = int(input())
x = int(input())
s = 0
t = 1
i = 1
while(i <= n):
       t = t * x
       s += t
       i += 1
print(s)