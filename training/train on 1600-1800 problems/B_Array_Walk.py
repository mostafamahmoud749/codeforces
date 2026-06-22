import sys 
sys.setrecursionlimit(100005)

def solve(r,l,s):
    if r+l==k:
        return 0
    if dp[r][l][s]!=-1:
        return dp[r][l][s]
    ch1=-float("inf")
    ch2=-float("inf")
    if r-l+1<n:
        ch1=a[r-l+1]+solve(r+1,l,0)
    if r-l-1>=0 and s!=1 and l<z:
        ch2=a[r-l-1]+solve(r,l+1,1)
    res=max(ch1,ch2)
    dp[r][l][s]=res
    return res

t=int(input())
for _ in range(t):
    n,k,z=map(int,input().split())
    a=list(map(int,input().split()))
    dp=[[[-1]*2 for _ in range(z+1)] for _ in range(k+1)]
    print(a[0]+solve(0,0,0))