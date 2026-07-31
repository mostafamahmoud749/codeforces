from collections import deque
import math

# def dfs(v):
#     for i in adj[v]:
#         if l[i]==-1:
#             l[i]=l[v]+1
#             dfs(i)


t=int(input())
for _ in range(t):
    n=int(input())
    a,b=map(int,input().split())

    adj=[[] for _ in range(n+1)]

    for i in range(n-1):
        x,y=map(int,input().split())
        adj[x].append(y)
        adj[y].append(x)

    l=[-1]*(n+1)
    parent=[-1]*(n+1)

    q=deque([a])
    l[a]=0

    while q:
        v=q.popleft()
        if v==b:
            break

        for i in adj[v]:
            if l[i]==-1:
                l[i]=l[v]+1
                parent[i]=v
                q.append(i)

    d=math.ceil(l[b]/2)
    m=b
    c=0
    cur=b
    while c<d:
        m=parent[cur]
        cur=parent[cur]
        c+=1
    
    l=[-1]*(n+1)

    # dfs(m)
    q=deque([m])
    l[m]=0
    maxl=0

    while q:
        v=q.popleft()
        maxl=max(maxl,l[v])
        for i in adj[v]:
            if l[i]==-1:
                l[i]=l[v]+1
                q.append(i)

    
    print(d+2*(n-1)-maxl)