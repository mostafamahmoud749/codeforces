def solve(num,cm):
    if dp[num][cm]!=-1:
        return dp[num][cm]
    if cm+num<10:
        dp[num][cm]=1
        return 1
    else:
        res=(solve(1,cm-(10-num))+solve(0,cm-(10-num)))%1000000007
        dp[num][cm]=res
        return res

t=int(input())
dp=[[-1]*200005 for _ in range(10)]

for i in range(200001):
    for j in range(10):
        solve(j,i)

for _ in range(t):
    n,m=map(str,input().split())
    m=int(m)
    res=0
    for i in range(len(n)):
        res=(res+dp[int(n[i])][m])%1000000007
    print(res)