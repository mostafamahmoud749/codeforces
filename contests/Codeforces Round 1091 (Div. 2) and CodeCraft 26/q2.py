import math
import heapq

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    s=int(input())
    x=a[s-1]
    pl=1 if x!=a[0] else 0
    pr=1 if x!=a[-1] else 0
    for i in range(1,s):
        if a[i-1]!=a[i]:
            pl+=1
    for i in range(s-1,n-1):
        if a[i]!=a[i+1]:
            pr+=1
    print(max(pr,pl))