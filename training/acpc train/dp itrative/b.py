import sys
sys.stdin = open('lepus.in','r')
sys.stdout = open('lepus.out','w')

n=int(input())
a=input()
dp=[0]*n
if a[n-1]=="w":
    print(-1)
    exit()
elif a[n-1]=="\"":
    dp[n-1]=1
for i in range(n-2,-1,-1):
    if a[i]=="w":
        dp[i]=-1
        continue
    dp[i]=dp[i+1]
    if i<n-3:
        dp[i]=max(dp[i],dp[i+3])
    if i<n-5:
        dp[i]=max(dp[i],dp[i+5])
    if dp[i]!=-1 and a[i]=="\"":
        dp[i]+=1
print(dp[0])
