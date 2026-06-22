def solve(indx,ch):
    if ch==0:
        return 0
    if indx<0:
        return float("inf")
    if dp[indx][ch]!=-1:
        return dp[indx][ch]
    ch2=float("inf")
    ch1=solve(indx-1,ch)
    if a[indx][1]<=ch:
        c=solve(indx-1,ch-a[indx][1])
        if c+a[indx][0]<=indx*x:
            ch2=c+a[indx][0]
    res=min(ch1,ch2)
    dp[indx][ch]=res
    return res


t=int(input())
for _ in range(t):
    m,x=map(int,input().split())
    th=0
    a=[]
    for i in range(m):
        c,h=map(int,input().split())
        th+=h
        a.append([c,h])
    dp=[[-1]*(th+1) for _ in range(m+1)]
    res=0
    tm=(m-1)*x+x
    for i in range(th,-1,-1):
        if solve(m-1,i)<=tm:
            res=i
            break
    print(res)