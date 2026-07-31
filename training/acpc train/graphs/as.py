from collections import deque

n,m=map(int,input().split())

adj=[set() for _ in range(n+1)]
l=[-1]*(n+1)

s=False
for i in range(m):
    x,y=map(int,input().split())
    adj[x].add(y)
    adj[y].add(x)
    if (x,y)==(1,n) or (x,y)==(n,1):
        s=True


if s:
    adj2=[[] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if (i!=j and i not in adj[j]):
                adj2[i].append(j)
                adj2[j].append(i)
    adj=adj2

q=deque([1])
l[1]=0

while q:
    v=q.popleft()
    for u in adj[v]:
        if l[u]==-1:
            l[u]=l[v]+1
            q.append(u)


print(l[n])