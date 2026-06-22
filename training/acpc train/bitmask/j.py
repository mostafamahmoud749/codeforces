t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    res=-1
    for i in range(n):
        if a[i]!=i:
            if res==-1:
                res=a[i]
            else:
                res&=a[i]
    print(0) if res==-1 else print(res)