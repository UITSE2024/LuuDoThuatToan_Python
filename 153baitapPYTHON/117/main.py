import math
n = int(input())
ahh = 0
if(n == 0):
    ahh = -1
if(n == 1):
    ahh = 3
att = -1
at = 3
t = 2
i = 2
while(i <= n):
    t *= 2
    ahh = 5*t + 5*at -att
    att = at
    at = ahh
    i +=1
print(ahh)
