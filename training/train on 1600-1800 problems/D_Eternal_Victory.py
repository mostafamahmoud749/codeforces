from collections import deque

n=int(input())
adj=[[] for _ in range(n+1)]

cost={}

tc=0

for _ in range(n-1):
    x,y,w=map(int,input().split())
    cost[(x,y)]=w
    cost[(y,x)]=w
    tc+=w
    adj[x].append(y)
    adj[y].append(x)

parent=[-1]*(n+1)
l=[-1]*(n+1)
l[1]=0

maxl=0
maxv=0

q=deque([1])
while q:
    v=q.popleft()
    if maxl<l[v]:
        maxl=l[v]
        maxv=v
    for i in adj[v]:
        if l[i]==-1:
            l[i]=l[v]+cost[(v,i)]
            q.append(i)
            parent[i]=v
    

path=set()
while parent[maxv]!=-1:
    path.add((parent[maxv],maxv))
    maxv=parent[maxv]

print(tc*2-maxl)
