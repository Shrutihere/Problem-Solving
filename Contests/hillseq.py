for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    d = {}
    res1 = []
    k = 0
    for i in arr:
        
        if i not in d.keys():
            d[i] = 1
            res1.append(i)
        else:
            d[i] += 1
            
            if i == arr[0] and d[i] == 2:
                print(-1)
                k = 1
                break
            if d[i] > 2:
                print(-1)
                k = 1
                break
            elif d[i]>1:
                res1.insert(0,i)
    if k == 0:
        print(*res1, sep=" ")
