from collections import deque

n,r1,r2=map(int,input().split())
a=list(map(int,input().split()))

adj=[[] for _ in range(n+1)]

parent=[-1]*(n+1)
visited=[False]*(n+1)

p=0
for i in range(n-1):
    if i+1==r1:
        p=1
    adj[a[i]].append(i+1+p)
    adj[i+1+p].append(a[i])



q=deque([r2])
visited[r2]=True

while q:
    v=q.popleft()
    for u in adj[v]:
        if not visited[u]:
            parent[u]=v
            visited[u]=True
            q.append(u)

# print(parent)
print(*parent[1:r2]+parent[r2+1:])