for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    if n == 1:
        print(0)
    else:
        c = 0
        for i in arr:
            if i%2 != 0:
                c+=1
        if c == 0 or c == 1:
            print(0)
        elif c%2 == 0:
            print(c//2)
        else:
            print((c-1)//2)
