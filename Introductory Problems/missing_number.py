n = int(input())
numbers_sum = sum(list(map(int, input().split(" "))))

"""
all_numbers = set([i for i in range(1, n+1)])

for n in numbers:
    all_numbers.remove(n)

print(*all_numbers)
"""

expected_sum = (n*(n+1))//2
total_sum = sum(numbers)
print(expected_sum - total_sum)