n = int(input())
arr = list(map(int, input().split()))
ops = 0
for i in range(1, n):
    if arr[i-1] > arr[i]:
        ops += arr[i-1]-arr[i]
        arr[i] = arr[i-1]

print(ops)