


n,k=map(int,input().split())
a=list(map(int,input().split()))

dp=[[False]*(k+1) for _ in range(k+1)]
dp[0][0]=True

for i in range(n):
    t1=k-a[i]
    for j in range(t1,-1,-1):
        for y in range(j,-1,-1):
            if dp[j][y]:
                dp[j+a[i]][y]=True
                dp[j+a[i]][y+a[i]]=True

res=[]
for i in range(k+1):
    if dp[k][i]:
        res.append(i)

print(len(res))
print(*res)