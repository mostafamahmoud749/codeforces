import sys
sys.setrecursionlimit(10**8)

def solve(curh,indx):
    if indx==n:
        return 0
    if db[curh][indx]!=-1:
        return db[curh][indx]
    
    r1=(curh+a[indx])%h
    r2=(curh+a[indx]-1)%h
    ch1=solve(r1,indx+1)
    ch2=solve(r2,indx+1)
    if l<=r1<=r:
        ch1+=1
    if l<=r2<=r:
        ch2+=1
    res=max(ch1,ch2)
    db[curh][indx]=res
    return res

n,h,l,r=map(int,input().split())
a=list(map(int,input().split()))
db=[[-1] * n for _ in range(h)]
res=solve(0,0)
print(res)