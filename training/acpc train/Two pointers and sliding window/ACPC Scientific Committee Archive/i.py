 
t=int(input())
for _ in range(t):
    n=int(input())
 
    dp=[[float("inf")]*(7) for _ in range(n+1)]
    dp[0][1]=0
 
    for i in range(1,n+1):
        for u in range(1,7):
            if u==1 or u==6:
               for j in range(1,7):
                    if (j!=1 and j!=6) and i-u>=0:
                        dp[i][u]=min(dp[i][u],1+dp[i-u][j])

            if u==2 or u==5:
                   for j in range(1,7):
                        if (j!=2 and j!=5) and i-u>=0:
                            dp[i][u]=min(dp[i][u],1+dp[i-u][j])
            if u==3 or u==4:
                   for j in range(1,7):
                        if (j!=3 and j!=4) and i-u>=0 :
                            dp[i][u]=min(dp[i][u],1+dp[i-u][j])
    res=float("inf")
    for j in range(1,7):
            res=min(res,dp[n][j])  
 
    # print(dp)
    if res==float("inf"):
         print(-1)
    else:
        print(res)  
 