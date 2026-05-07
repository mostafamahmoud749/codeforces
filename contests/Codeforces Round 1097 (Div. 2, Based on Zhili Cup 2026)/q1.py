t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    res=1 if a[-1]>0 else 0
    for i in range(n-2,-1,-1):
        if a[i+1]>0:
            a[i]=a[i]+a[i+1]
        if a[i]>0: 
            res+=1
    print(res)