

t=int(input())
for _ in range(t):
    n,m,q=map(int,input().split())
    b=sorted(map(int,input().split()))
    q=list(map(int,input().split()))

    for i in range(len(q)):
        res1=-1
        l=0
        r=len(b)-1
        while l<=r:
            mid=l+(r-l)//2
            if b[mid]<q[i]:
                l=mid+1
                res1=mid
            else:
                r=mid-1
        
        res2=-1
        l=0
        r=len(b)-1
        while l<=r:
            mid=l+(r-l)//2
            if b[mid]>q[i]:
                r=mid-1
                res2=mid
            else:
                l=mid+1
        
        # print(res1,res2)

        if res2==-1:
            print(n-b[res1])
        elif res1==-1:
            print(b[res2]-1)
        else:
            print((b[res2]-b[res1])//2)