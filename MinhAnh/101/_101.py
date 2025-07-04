s=0
e=1
i=1
while(e>=10**-6):
    e=1/i
    s+=e
    i+=1
print(s)
