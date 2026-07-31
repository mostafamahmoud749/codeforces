from collections import deque


n=int(input())

adj=[[] for _ in range(n+1)]

for _ in range(n-1):
    x,y,t=map(int,input().split())
    adj[x].append((y,t))
    adj[y].append((x,t))

visited=[False]*(n+1)

q=deque([(1,-1)])
visited[1]=True

res=set()

while q:
    v,lb=q.popleft()

    for i,t in adj[v]:
        if not visited[i]:
            if t==1:
                q.append((i,lb))
                visited[i]=True
            else:
                if lb!=-1:
                    res.discard(lb)
                res.add(i)
                visited[i]=True
                q.append((i,i))

print(len(res))
print(*res)

