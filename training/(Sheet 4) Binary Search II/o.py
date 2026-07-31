
t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split())
    l=1
    r=m
    res=0
    while l<=r:
        mid=l+(r-l)//2
        if n*((m//(mid+1))*mid+(m%(mid+1)))>=k:
            res=mid
            r=mid-1
        else:
            l=mid+1

    print(res)
