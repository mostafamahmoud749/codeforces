from collections import deque

n=int(input())
a=list(map(int,input().split()))

adj=[[] for _ in range(n+1)]
visited=[False]*(n+1)

for i in range(n):
    adj[a[i]].append(i+1)
    adj[i+1].append(a[i])

res=0

for i in range(1,n+1):
    if not visited[i]:
        res+=1
        q=deque([i])
        visited[i]=True

        while q:
            v=q.popleft()
            for u in adj[v]:
                if not visited[u]:
                    visited[u]=True
                    q.append(u)

print(res)