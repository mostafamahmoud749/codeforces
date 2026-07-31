from collections import deque

n=int(input())

adj={}
visited=set()
parents={}


for i in range(n):
    x,y=map(int,input().split())
    if x in adj:
        adj[x].append(y)
    else:
        adj[x]=[y]
    if y in adj:
            adj[y].append(x)
    else:
        adj[y]=[x]

s=-1
e=-1
for i in adj.keys():
    if s==-1 and len(adj[i])==1:
        s=i
    elif e==-1 and len(adj[i])==1:
        e=i
        break
# print(s,e)

visited.add(s)
q=deque([s])


while q:
    v=q.popleft()
    for u in adj[v]:
        if u not in visited:
            visited.add(u)
            parents[u]=v
            q.append(u)

res=[]

v=e
while v in parents:
    res.append(v)
    v=parents[v]

res.append(s)

print(*res)