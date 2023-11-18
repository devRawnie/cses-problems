n = int(input())

if n == 1:
    print(1)

elif n < 5:
    print("NO SOLUTION")

else:
    i = 1
    while i <= n:
        print(i, end=" ")
        i += 2

    i = 2
    while i <= n:
        print(i, end=" ")
        i += 2