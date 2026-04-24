import math
import heapq

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    heapq.heapify(a)
    res=-float("inf")
    while len(a)>0:
        v=heapq.heappop(a)
        res=max(res,v)
        for i in range(len(a)):
            a[i]=a[i]-v
    print(res)