# def solve(indx,rem,pmax):
#     if indx>k:
#         return (n-p[pmax])*pmax
#     if rem<0:
#         return -float("inf")
#     if dp[indx][rem][pmax] != -1:
#         return dp[indx][rem][pmax]
    
#     ch1=solve(indx+1,rem,pmax)

#     ch2=-float("inf")
#     if indx<=rem and p[indx]!=-1 and p[indx]>=p[pmax]:
#         ch2=solve(indx+1,rem-indx,indx)+(p[indx]-p[pmax])*pmax

#     res=max(ch1,ch2)
#     dp[indx][rem][pmax]=res
#     return res

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))

    p=[-1]*(k+1)
    p[0]=0

    c=1
    for i in range(n):
        while c<=k and c<=a[i]:
            p[c]=i
            c+=1

    dp=[[-1]*(k+1) for _ in range(k+1)]
    dp[0][0]=0

    for spent in range(k+1):
        for pmax in range(k+1):
            if dp[spent][pmax]==-1:
                continue
            for b in range(spent+1,k+1):
                if spent+b>k:
                    break
                if p[b]==n:
                    continue
                v=dp[spent][pmax]+pmax*(p[b]-p[pmax])
                if v>dp[spent+b][b]:
                    dp[spent+b][b]=dp[spent][pmax]+v











# t=int(input())
# for _ in range(t):
#     n,k=map(int,input().split())
#     a=list(map(int,input().split()))

#     dp=[[-1] * (k+1) for _ in range(n)]

#     for i in range(min(k,a[0])+1):
#         dp[0][i]=i

#     for i in range(1,n):
#         maxv=-1
#         for j in range(k+1):
#             if dp[i-1][j]!=-1:
#                 dp[i][j]=dp[i-1][j]+j

#             if j>0 and dp[i-1][j-1]!=-1:
#                 maxv = max(maxv,dp[i-1][j-1])

#             if j<=a[i] and maxv!=-1:
#                 dp[i][j]=max(dp[i][j],maxv+j)

#     print(max(dp[n-1]))