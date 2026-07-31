from collections import deque

t=int(input())
for _ in range(t):
    n,m,k,d=map(int,input().split())
    res=[]
    for y in range(n):
        a=list(map(int,input().split()))

        dp=[float("inf")]*m
        dp[0]=1

        dq=deque([0])
        for i in range(1,m):
            if dq[0]<i-d-1:
                dq.popleft()

            dp[i]=dp[dq[0]]+a[i]+1

            while dq and dp[dq[-1]]>=dp[i]:
                dq.pop()
            dq.append(i)
        
        res.append(dp[m-1])
    
    out=sum(res[:k])
    cur=out
    for i in range(k,n):
        cur+=res[i]-res[i-k]
        out=min(out,cur)

    print(out)