import math
n = int(input())
s = 0
i = 1
while(i <= n):
    s = s + i/(math.sqrt(i) + math.sqrt(i+1))
    i+=1
print(s)
