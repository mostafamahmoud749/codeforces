from collections import deque


n,k,d=map(int,input().split())

adj=[[] for _ in range(n+1)]

a=list(map(int,input().split()))

for i in range(1,n):
    x,y=map(int,input().split())
    adj[x].append((y,i))
    adj[y].append((x,i))


q=deque([])
visited=[False]*(n+1)
for i in a:
    q.append(i)
    visited[i]=True

used=[False]*n

while q:
    v=q.popleft()
    for i in adj[v]:
        if not visited[i[0]]:
            visited[i[0]]=True
            used[i[1]]=True
            q.append(i[0])

res=[]
for i in range(1,n):
    if not used[i]:
        res.append(i)

print(len(res))
print(*res)


