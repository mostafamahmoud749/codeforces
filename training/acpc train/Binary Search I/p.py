t=int(input())
for _ in range(t):
    n,k,q=map(int,input().split())
    a=[0]+list(map(int,input().split()))
    b=[0]+list(map(int,input().split()))
    out=[]
    for i in range(q):
        d=int(input())
        l=0
        r=k
        res=0
        while l<=r:
            mid=l+(r-l)//2
            if a[mid]>=d:
                res=mid
                r=mid-1
            else:
                l=mid+1
        out.append(b[res-1]+(d-a[res-1])*(b[res]-b[res-1])//(a[res]-a[res-1]))
    print(*out)