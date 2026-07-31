from collections import deque
import heapq
import math

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))

    adj=[[] for _ in range(n+1)]

    for i in range(n-1):
        adj[i+2].append(a[i])
        adj[a[i]].append(i+2)

    visited=[False]*(n+1)

    q=deque([1])
    visited[1]=True

    while q:
        v=q.popleft()
        # check for leafs under v
        lf=[]
        for i in adj[q]:
            if len(adj[i])==0:
                lf.append(i)
            