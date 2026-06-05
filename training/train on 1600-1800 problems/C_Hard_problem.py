import sys
sys.setrecursionlimit(300005)

def solve(indx,ls):
    if indx==n+1:
        return 0
    if dp[indx][ls]!=-1:
        return dp[indx][ls]
    ch1=float("inf")
    ch2=float("inf")
    if ls==0:
        if s[indx]>=s[indx-1]:
            ch1=solve(indx+1,0)
        if s[indx][::-1]>=s[indx-1]:
            ch2=a[indx-1]+solve(indx+1,1)
    if ls==1:
        if s[indx]>=s[indx-1][::-1]:
            ch1=solve(indx+1,0)
        if s[indx][::-1]>=s[indx-1][::-1]:
            ch2=a[indx-1]+solve(indx+1,1)
    res=min(ch1,ch2)
    dp[indx][ls]=res
    return res


n=int(input())
a=list(map(int,input().split()))
s=[""]*(n+1)
for i in range(1,n+1):
    s[i]=input()
dp=[[-1]*2 for _ in range(n+1)]
res=solve(1,0)
print(res) if res!=float("inf") else print(-1)
