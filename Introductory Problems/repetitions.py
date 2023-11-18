dna = input()
"""
a = 0
b = a + 1

x = 1
while b < len(dna):
    if dna[a] != dna[b]:
        x = max(x, b - a)
        a = b

    b += 1

x = max(x, b-a)
print(x)
"""
gm = 0
s = 1
for i in range(1, len(dna)):
    if dna[i-1] == dna[i]:
        s += 1
    else:
        s = 1

    if s > gm:
        gm = s

print(gm)