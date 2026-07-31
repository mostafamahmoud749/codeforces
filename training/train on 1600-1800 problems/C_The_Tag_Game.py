from collections import deque

n,s=map(int,input().split())

adj=[[] for _ in range(n+1)]

for _ in range(n-1):
    x,y=map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)

l1=[-1]*(n+1)
q=deque([1])
l1[1]=0

while q:
    v=q.popleft()
    for i in adj[v]:
        if l1[i]==-1:
            l1[i]=l1[v]+1
            q.append(i)

l2=[-1]*(n+1)
q=deque([s])
l2[s]=0

while q:
    v=q.popleft()
    for i in adj[v]:
        if l2[i]==-1:
            l2[i]=l2[v]+1
            q.append(i)

res=0
for i in range(1,n+1):
    if l1[i]>l2[i]:
        res=max(res,l1[i])

print(res*2)