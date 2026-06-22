t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    dp=[[0]*31 for x in range(n)]

    for j in range(31):
        ch1=0
        if j<30:
            ch1=a[n-1]//2**(j+1)
        ch2=a[n-1]//2**(j)-k
        dp[n-1][j]=max(ch1,ch2)

    for i in range(n-2,-1,-1):
        for j in range(0,31):
            ch1=0
            if j<30:
                ch1=dp[i+1][j+1]+a[i]//2**(j+1)
            ch2=dp[i+1][j]-k+a[i]//2**(j)
            dp[i][j]=max(ch1,ch2)
    print(dp[0][0])



