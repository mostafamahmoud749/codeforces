t=int(input())
for _ in range(t):
    n = int(input())
    a=list(map(int,input().split()))
        
    db=[0]*n
    for i in range(n):
        db[a[i]-1] = i
    ms=0
    c=0
    for k in range(n + 1):
        s = k - c
        if s > ms:
            ms = s
        if k < n:
            if db[k] < k:
                c += 1
    print(ms)

