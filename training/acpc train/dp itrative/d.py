import sys
sys.stdin = open('king2.in','r')
sys.stdout = open('king2.out','w')

a=[list(map(int,input().split())) for _ in range(8)]
dp=[[0]*8 for _ in range(8)]
for i in range(8):
    for j in range(7,-1,-1):
        ch1=float("inf")
        ch2=float("inf")
        ch3=float("inf")
        if i>0 and j<7:
            ch1=dp[i-1][j+1]
        if i>0:
            ch2=dp[i-1][j]
        if j<7:
            ch3=dp[i][j+1]
        dp[i][j]=min(ch1,ch2,ch3)+a[i][j] if min(ch1,ch2,ch3)!=float("inf") else a[i][j]

print(dp[7][0])