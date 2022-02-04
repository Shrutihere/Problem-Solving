for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    
    count = 0
    count += n-a[0]
    count += n-b[1]-min(b[0],a[1])
    
    print(count)
