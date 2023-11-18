n = int(input())
numbers = list(map(int, input().split(" ")))

all_numbers = set([i for i in range(1, n+1)])

for n in numbers:
    if n not in all_numbers:
        print(n)
        break
    else:
        all_numbers.remove(n)
    