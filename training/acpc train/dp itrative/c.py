# import sys
# sys.stdin = open('knight.in','r')
# sys.stdout = open('knight.out','w')

n,m=map(int,input().split())
dp=[[-1] *(m) for _ in range(n)]
dp[n-1][m-1]=0

for i in range(n-1,-1,-1):
    for j in range(m-1,-1,-1):
        ch1=-1
        ch2=-1
        if i<n-1 and j<m-2 and dp[i+1][j+2]!=-1:
            ch1=1+dp[i+1][j+2]
        if j<m-1 and i<n-2 and dp[i+2][j+1]!=-1:
            ch2=1+dp[i+2][j+1]
        if ch1!=-1:dp[i][j]+=ch1
        if ch2!=-1:dp[i][j]+=ch2

print(0 if dp[0][0]==-1 else dp[0][0]+1)