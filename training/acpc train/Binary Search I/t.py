n=int(input())
a=list(map(int,input().split()))
p=[0]*(n+1)
for i in range(1,n+1):
    p[i]=p[i-1]+a[i-1]
m=int(input())
b=list(map(int,input().split()))
for q in b:
    l,r=1,n
    ans=1
    while l <= r:
        mid=(l+r)//2
        if p[mid]>=q:
            ans=mid
            r=mid-1
        else:
            l=mid+1
    print(ans)