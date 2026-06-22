# import sys
# sys.stdin = open('slalom.in','r')
# sys.stdout = open('slalom.out','w')

n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
dp=[[0]*n for _ in range(n)]

for j in range(n):
    dp[n-1][j]=a[n-1][j]

for i in range(n-2,-1,-1):
    for j in range(i,-1,-1):
        ch1=dp[i+1][j]
        ch2=dp[i+1][j+1]
        dp[i][j]=max(ch1,ch2)+a[i][j]
print(dp[0][0])