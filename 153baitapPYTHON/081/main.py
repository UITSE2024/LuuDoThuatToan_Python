n = int(input())
x = int(input())
s = 0
m = 1
i = 0
while(i <= n):
       m= m * (x+1)
       s += 1/m
       i += 1
print(s)