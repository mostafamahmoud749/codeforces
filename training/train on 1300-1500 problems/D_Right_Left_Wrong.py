t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    s=input()
    l=0
    r=n-1
    p=[0]*(n+1)
    res=0
    for i in range(1,n+1):
        p[i]=p[i-1]+a[i-1]
    while l<r:
        if s[l]!="L":
            l+=1
        if s[r]!="R":
            r-=1
        if s[l]=="L" and s[r]=="R":
            res+=p[r+1]-p[l]
            r-=1
            l+=1
    print(res)