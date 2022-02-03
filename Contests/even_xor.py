import math
for _ in range(int(input())):
    n = int(input())
    arr = [3]
    x = 3
    for i in range(1,n):
        x+=1
        while bin(x)[2:].count('1')%2 != 0:
            x+=1
        arr.append(x)
    for i in arr:
        print(i, end=" ")
    print()
