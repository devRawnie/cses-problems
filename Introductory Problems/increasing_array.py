input()

arr = list(map(int, input().split()))

ops = 0
for i in range(1, len(arr)):
    if arr[i] < arr[i-1]:
        ops = ops + (arr[i-1]+arr[i])
        arr[i] = arr[i-1]

print(ops)