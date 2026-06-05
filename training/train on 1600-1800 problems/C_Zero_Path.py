import sys
sys.setrecursionlimit(2005)

def solve(x,y):
    if y==m-1 and x==n-1:
        return a[x][y],a[x][y]
    if dp[x][y]!=-1:
        return dp[x][y]
    ch1max,ch1min=-float("inf"),float("inf")
    ch2max,ch2min=-float("inf"),float("inf")
    if x+1<n:
        ch1max,ch1min=solve(x+1,y)
    if y+1<m:
        ch2max,ch2min=solve(x,y+1)
    cmax=max(ch1max,ch2max)+a[x][y]
    cmin=min(ch1min,ch2min)+a[x][y]
    res=(cmax,cmin)
    dp[x][y]=res
    return res

t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=[]
    for _ in range(n):
        a.append(list(map(int,input().split())))
    dp=[[-1]* m for _ in range(n)]
    if (n+m-1)%2!=0:
        print("NO")
        continue
    rmax,rmin=solve(0,0)
    print("YES") if rmax>=0>=rmin else print("NO")