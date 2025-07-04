import math
n = int(input())
s = 0
m = 0
e = 1
i = 0
while(i <= n):
       m += i
       e = 1/m
       s += e
       i +=1
print(s)
