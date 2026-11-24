from collections import deque


n,m,k=map(int,input().split())
c=list(map(int,input().split()))

adj=[[] for _ in range(n+1)]

for _ in range(m):
  l,r=map(int,input().split())
  adj[l].append(r)
  adj[r].append(l)

visited=[False] * (n+1)

res=0
for i in range(1,n+1):
  if not visited[i]:
    cnt=0
    lst={}
    mx=0

    visited[i]=True
    q=deque([i])

    while q:
      v=q.popleft()
      clr=c[v-1]
      if clr in lst:
        lst[clr]+=1
      else:
        lst[clr]=1
      mx=max(lst[clr],mx)
      cnt+=1

      for u in adj[v]:
        if not visited[u]:
          q.append(u)
          visited[u]=True

    res+=(cnt-mx)

print(res)



