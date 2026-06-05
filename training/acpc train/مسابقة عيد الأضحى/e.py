def solve(indx,cs):
    global s
    if indx==n:
        if cs==0:
            return 1
        return 0
    if dp[indx][cs]!=-1:
        return dp[indx][cs]
    ch1=solve(indx+1,cs)
    ch2=0
    if a[indx]<=cs:
        ch2=solve(indx+1,cs-a[indx])
    res=ch1+ch2
    dp[indx][cs]=res
    return res

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    dp=[[-1]*2 for _ in range(n)]
    s=sum(a)
    res=solve(0,1)
    print(res)
