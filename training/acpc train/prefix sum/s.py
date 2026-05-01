
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    p=[0]*n
    res=0
    indx=0
    for i in range(1,n):
        p[i]=p[i-1]
        if i<n-1 and a[i-1]<a[i] and a[i]>a[i+1]:
            p[i]+=1

    for l in range(0,n-k+1):
        r=l+k-1
        cur=p[r-1]-p[l]
        if cur>res:
            indx=l
        res=max(res,cur)
    print(res+1,indx+1)