from collections import deque

n=int(input())
k=int(input())

adj=[[] for _ in range(n+1)]
visited=[False]*(n+1)

for i in range(k):
    x,y=map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)

res=0
comp=0
b=[-1]*(n+1)
res=[0]*(n+1)

for i in range(1,n+1):
    if not visited[i]:
        size=0
        comp+=1
        q=deque([i])
        visited[i]=True

        while q:
            v=q.popleft()
            size+=1
            b[v]=comp
            for u in adj[v]:
                if not visited[u]:
                    visited[u]=True
                    q.append(u)
        res[comp]=size

k=int(input())
for _ in range(k):
    x,y=map(int,input().split())
    if b[x]==b[y]:
        res[b[x]]=0

print(max(res))