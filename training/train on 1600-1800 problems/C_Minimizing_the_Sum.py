import sys
sys.setrecursionlimit(300000)

def solve(indx,curk):
    if indx==n:
        return 0
    if dp[indx][curk]!=-1:
        return dp[indx][curk]
    res=0
    curmin=a[indx]
    cursum=0
    for i in range(indx,min(n,indx+curk+1)):
        curmin=min(curmin,a[i])
        cursum+=a[i]
        res=max(res,cursum-((i-indx+1)*curmin)+solve(i+1,curk-(i-indx)))
    dp[indx][curk]=res
    return res

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    dp=[[-1]*(k+1) for _ in range(n+1)]
    print(sum(a)-solve(0,k))