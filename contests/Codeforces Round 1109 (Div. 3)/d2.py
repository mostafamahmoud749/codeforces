import sys
from collections import deque
import heapq
import math
# sys.setrecursionlimit(200005)

# def solve(indx,s):
#     if indx<0:
#         return 0
#     if dp[indx][s]!=-1:
#         return dp[indx][s]
    
#     ch2=-float("inf")
#     if s==0:
#         ch1=a[indx]+solve(indx-1,s)
#         if nb[indx+1]:
#             ch2=-a[indx]+solve(indx-1,1-s)
#     else:
#         ch1=-a[indx]+solve(indx-1,s)
#         if nb[indx+1]:
#             ch2=a[indx]+solve(indx-1,1-s)
    
#     res=max(ch1,ch2)
#     dp[indx][s]=res
#     return res


t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))

    nb=[False]*(n+1)
    for i in range(m):
        nb[b[i]]=True
    
    dp=[[-float("inf")]*(2) for j in range(n+1)]

    dp[0][0]=0
    dp[0][1]=0

    for i in range(1,n+1):
        dp[i][0]=a[i-1]+dp[i-1][0]
        if nb[i]:
            dp[i][0]=max(dp[i][0],-a[i-1]+dp[i-1][1])

        dp[i][1]=-a[i-1]+dp[i-1][1]
        if nb[i]:
            dp[i][1]=max(dp[i][1],a[i-1]+dp[i-1][0])

    print(dp[n][0])