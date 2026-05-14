import sys
sys.setrecursionlimit(200000)

def dfs(u):
    visted[u] = 1
    for v in ver[u]:
        if visted[v] == 0:
            dfs(v)

n,m=map(int,input().split())
a=list(map(int,input().split()))
ver=[[] for i in range(n)]
visted=[0]*n
per=[]
for i in range(n):
    per.append([a[i],i])
per.sort()
res=0
for i in range(m):
    u,v=map(int,input().split())
    u-=1
    v-=1
    ver[u].append(v)
    ver[v].append(u)
for i in range(n):
    if visted[per[i][1]]!=1:
        res+=per[i][0]
        dfs(per[i][1])
print(res)