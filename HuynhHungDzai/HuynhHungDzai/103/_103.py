s = 0
e = 1
i = 1
epsilon = 1**-6

while(e >= epsilon):
    e = 1/i 
    s += e
    i += 2

print("Gia tri cua s: {:.2f}".format(s))

