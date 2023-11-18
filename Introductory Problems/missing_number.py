n = int(input())
numbers = list(map(int, input().split(" ")))

all_numbers = set([i for i in range(1, n+1)])

for n in numbers:
    all_numbers.remove(n)

print(*a)