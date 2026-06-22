import sys
sys.setrecursionlimit(300000)
from _bisect import bisect_right

def solve(indx):
    if indx>=n:
        return []
    if dp[indx]!=-1:
        return dp[indx]
    ch1=[]
    ch2=[]
    if a[indx]+1 in exist:
        l=exist[a[indx]+1]
        v=bisect_right(l,indx)
        if v<len(l):
            ch1=[indx+1]+solve(l[v])
    ch2=solve(indx+1)
    if len(ch1)>=len(ch2):
        res=ch1
    else:res=ch2
    dp[indx]=res
    return res


n=int(input())
a=list((map(int,input().split())))
dp=[-1]*(n+1)
exist={}
for i in range(n):
    if a[i] not in exist:
        exist[a[i]]=[]
    exist[a[i]].append(i)
res=solve(0)
print(len(res))
print(*res)