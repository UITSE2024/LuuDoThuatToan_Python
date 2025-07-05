n = int(input())

at = 2
bt = 1
i = 2
ahh = -1
bhh = -1

while i <= n:
    ahh = at ** 2 + 2 * bt ** 2
    bhh = 2 * at * bt
    i = i + 1
    at = ahh
    bt = bhh

print(ahh, bhh)