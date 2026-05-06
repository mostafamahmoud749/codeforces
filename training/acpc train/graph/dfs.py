def dfs(u):
    visted[u] = 1
    print(u+1)
    for v in ver[u]:
        if visted[v] == 0:
            dfs(v)

n,m=map(int,input().split())
ver=[[] for i in range(n)]
visted=[0]*n
for i in range(m):
    u,v=map(int,input().split())
    u-=1
    v-=1
    ver[u].append(v)
    ver[v].append(u)

print(ver)
dfs(4)