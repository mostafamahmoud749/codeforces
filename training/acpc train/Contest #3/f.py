import sys
input = sys.stdin.readline

n,m=map(int,input().split())
t=sorted(map(int,input().split()))
a=list(map(int,input().split()))
boxes=[]
for i in range(0,n,500):
    boxes.append(t[i:i+500])
for i in range(m):
    l=0
    r=len(boxes)-1
    res=-1
    while l<=r:
        mid=l+(r-l)//2
        if a[i]>=boxes[mid][0]:
            res=mid
            l=mid+1
        else:
            r=mid-1
    ans=-1
    if res!=-1:
        l2=0
        r2=len(boxes[res])-1
        res2=-1
        while l2<=r2:
            mid=l2+(r2-l2)//2
            if a[i]>=boxes[res][mid]:
                res2=mid
                l2=mid+1
            else:
                r2=mid-1
        if res2!=-1:
            ans=boxes[res].pop(res2)
            if not boxes[res]:
                boxes.pop(res)
    print(ans)