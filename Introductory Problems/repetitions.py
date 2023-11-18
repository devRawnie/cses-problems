dna = input()

a = 0
b = a + 1

x = 1
while b < len(dna):
    if dna[a] != dna[b]:
        x = max(x, b - a)
        a = b

    b += 1

print(x)
