import math
for _ in range(int(input())):
    n = int(input())
    count = 0
    # ans = math.log10(n) /math.log10(2)
    if n%2==0:
        while n>0 and n%2==0:
            count += 1
            n = n//2
    elif n == 1:
        count = 1
    else:
        count = 0
    print(count)
