import heapq

n,m=map(int,input().split())

adj=[[] for _ in range(n+1)]

for _ in range(m):
    x,y,w=map(int,input().split())
    adj[x].append([y,w])
    adj[y].append([x,w])

parent=[-1]*(n+1)
l=[float("inf")]*(n+1)
l[1]=0

q=[[0,1]]

while q:
    c,v=heapq.heappop(q)
    if c!=l[v]:
        continue

    for i in adj[v]:
        nc=c+i[1]
        if nc<l[i[0]]:
            l[i[0]]=nc
            parent[i[0]]=v
            heapq.heappush(q,[nc,i[0]])

res=[]
v=n

if l[n]==float('inf'):
    print(-1)
else:
    while v!=-1:
        res.append(v)
        if v==1:
            break
        v=parent[v]

    res.reverse()
    print(*res)