s = 0
e = 0.5
i = 1

while e >= 1e-6:
    e = 1 / (i * (i + 1))
    s = s + e
    i = i + 1

print(f"S = {s:.2f}")