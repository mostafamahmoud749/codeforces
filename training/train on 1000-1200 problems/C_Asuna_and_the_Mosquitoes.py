t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    op=[0]*(n+1)
    ep=[0]*(n+1)
    for i in range(1,n+1):
        if a[i-1]%2==0:
            ep[i]=ep[i-1]+1
            op[i]=op[i-1]
        else:
            op[i]=op[i-1]+1
            ep[i]=ep[i-1]
    res=0
    if op[n]==0 or ep[n]==0:
        res=max(a)
    else:
        res=sum(a)-op[n]+1
    print(res)