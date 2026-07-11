import heapq

n,m=map(int,input().split())
adj=[[] for _ in range(n+1)]
visited=[False]*(n+1)
visited[1]=True

for _ in range(m):
    x,y=map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)

q=[1]
res=[]

while q:
    v=heapq.heappop(q)
    res.append(v)
    for i in adj[v]:
        if not visited[i]:
            visited[i]=True
            heapq.heappush(q,i)

print(*res)