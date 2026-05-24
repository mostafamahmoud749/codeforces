import sys
sys.setrecursionlimit(300000)

def solve(indx):
    if indx==n:
        return 0
    if db[indx]!=-1:
        return db[indx]
    if indx+a[indx]+1<=n:
        ch1=solve(indx+a[indx]+1)
    else:
        ch1=n-indx+a[indx]+1
    ch2=1+solve(indx+1)
    res=min(ch1,ch2)
    db[indx]=res
    return res

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    db=[-1]*n
    res=solve(0)
    print(res)