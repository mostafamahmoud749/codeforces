def solve(s,sd):
    if s==n and sd==1:
        return 1
    if s>=n:
        return 0
    if dp[s][sd]!=-1:
        return dp[s][sd]
    res=0
    for i in range(1,k+1):
        if i>=d:
            res+=solve(s+i,1)
        else:
            res+=solve(s+i,sd)
    res=res%1000000007
    dp[s][sd]=res
    return res

n,k,d=map(int,input().split())
dp=[[-1] * 2 for _ in range(n+1)]
res=solve(0,0)
print(res)