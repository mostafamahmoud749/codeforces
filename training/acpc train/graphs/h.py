from collections import deque

n,m=map(int,input().split())

adj=[[] for _ in range(n+1)]
visited=[False]*(n+1)

for i in range(m):
    x,y=map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)

res=1


for i in range(1,n+1):
    if not visited[i]:
        cres=1
        q=deque([i])
        visited[i]=True

        while q:
            v=q.popleft()
            if v!=i:
                cres*=2
            for u in adj[v]:
                if not visited[u]:
                    visited[u]=True
                    q.append(u)
        res*=cres

print(res)