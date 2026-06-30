n=int(input())
a=[]
b=[]

for _ in range(n):
    x,y=map(int,input().split())
    a.append(x)
    b.append(y)
capacty=sum(a)
water=sum(b)

dp=[[-1]*(capacty+1) for _ in range(n+1)]
dp[0][0]=0

for x in range(n):
    for i in range(n,0,-1):
        for j in range(capacty,a[x]-1,-1):
            if dp[i-1][j-a[x]]!=-1:
                dp[i][j]=max(dp[i][j],dp[i-1][j-a[x]]+b[x])

res=[]
for k in range(1,n+1):
    cres=0
    for j in range(capacty+1):
        if dp[k][j]!=-1:
            cwater=water-dp[k][j]
            cres=max(cres,min(j,dp[k][j]+cwater/2))
    res.append(cres)

for i in range(len(res)):
    res[i]=f"{res[i]:.10f}"

print(*res)