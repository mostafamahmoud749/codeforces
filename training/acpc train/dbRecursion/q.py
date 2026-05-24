import sys
sys.setrecursionlimit(300005)

def solve(indx,s):
    if indx>=n:
        return 0
    if db[indx][s%2]!=-1:
        return db[indx][s%2]
    ch1=float("inf")
    ch2=float("inf")
    if s%2!=0:
        ch1=solve(indx+1,s+1)
        ch2=solve(indx+2,s+1)
    else:
        ch1=a[indx]+solve(indx+1,s+1)
        if indx+1<n:
            ch2=a[indx]+a[indx+1]+solve(indx+2,s+1)
    res=min(ch1,ch2)
    db[indx][s%2]=res
    return res

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    db=[[-1] * (2) for _ in range(n)]
    res=solve(0,0)
    print(res)
