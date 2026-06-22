def solve(indx,ck):
    if indx==n:
        return 0
    if dp[indx][ck]!=-1:
        return dp[indx][ck]
    res=float("inf")
    for i in range(indx+1,n+1):
        r=i-indx-1
        if ck+r<=k:
            res=min(res,a[indx]*(d[i]-d[indx])+solve(i,ck+r))
    dp[indx][ck]=res
    return res

n,l,k=map(int,input().split())
d=list(map(int,input().split()))+[l]
a=list(map(int,input().split()))+[0]
dp=[[-1]*n for _ in range(n)]
print(solve(0,0))