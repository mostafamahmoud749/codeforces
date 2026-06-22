import sys
sys.setrecursionlimit(100005)

def solve(indx,s):
    if indx==n:
        return 0
    if  dp[indx][s]!=-1: 
        return dp[indx][s]
    if s==0:
        ch1=b[indx]+solve(indx+1,1)
        ch2=solve(indx+1,0)
    else:
        ch1=a[indx]+solve(indx+1,0)
        ch2=solve(indx+1,1)
    res=max(ch1,ch2)
    dp[indx][s]=res
    return res

n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
dp=[[-1]*2 for _ in range(n+1)]
print(max(solve(0,0),solve(0,1)))

