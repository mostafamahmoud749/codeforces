n,m=map(int,input().split())

adj=[set() for _ in range(n+1)]
deg=[0]*(n+1)
e=[]

for _ in range(m):
    x,y=map(int,input().split())
    deg[x]+=1
    deg[y]+=1
    adj[x].add(y)
    adj[y].add(x)
    e.append((x,y))


a=[[] for _ in range(n+1)]

res=float("inf")

for i in e:
    for j in range(1,n+1):
        if j!=i[0] and j!=i[1] and j in adj[i[0]] and j in adj[i[1]]:
            res=min(res,(deg[i[0]]+deg[i[1]]+deg[j]-6))

print(res) if res!=float("inf") else print(-1)