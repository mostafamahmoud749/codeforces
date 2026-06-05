import sys
sys.setrecursionlimit(5005)

def solve(n):
    if n==0:
        return 0
    if dp[n]!=-1:
        return dp[n]
    ch1=-float("inf")
    ch2=-float("inf")
    ch3=-float("inf")
    if n>=a:
        ch1=1+solve(n-a)
    if n>=b:
        ch2=1+solve(n-b)
    if n>=c:
        ch3=1+solve(n-c)
    res=max(ch1,ch2,ch3)
    dp[n]=res
    return res


n,a,b,c=map(int,input().split())
dp=[-1 for _ in range(n+1)]
res=solve(n)
print(res)
