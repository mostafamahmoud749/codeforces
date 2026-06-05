import sys
sys.setrecursionlimit(5005)

def solve(l,r):
    if l>=r:
        return 0
    if dp[l][r]!=-1:
        return dp[l][r]
    ch1=1+solve(l+1,r)
    ch2=1+solve(l,r-1)
    ch3=float("inf")
    if newa[l]==newa[r]:
        ch3=1+solve(l+1,r-1)
    res=min(ch1,ch2,ch3)
    dp[l][r]=res
    return res

n=int(input())
a=list(map(int,input().split()))
newa=[a[0]]
res=float("inf")
for i in range(1,n):
    if a[i]!=a[i-1]:
        newa.append(a[i])
dp=[[-1]*len(newa) for _ in range(len(newa))]
res=solve(0,len(newa)-1)
print(res)