def dfs(i,l,d):
    global res
    depth[i]=d
    for u in adj[i]:
        if u in visited and l!=u:
            res=min(res,depth[i]-depth[u]+1)
        if u not in visited:
            visited.add(u)
            dfs(u,i,d+1)

n=int(input())

a=list(map(int,input().split()))
na=[]
for i in a:
    if i!=0:
        na.append(i)

if len(na)>128:
    print(3)
    exit()

adj={}
for i in range(len(na)):
    adj[i]=[]

for i in range(len(na)):
    for j in range(i+1,len(na)):
        if (na[i]&na[j])!=0:
            adj[i].append(j)
            adj[j].append(i)



res=float("inf")

for i in range(len(na)):
    visited=set()
    visited.add(i)
    depth={}
    
    dfs(i,-1,0)

print(res) if res!=float("inf") else print(-1)