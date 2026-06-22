t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    res=a[0]
    for i in range(1,n):
        res&=a[i]
    print(res)