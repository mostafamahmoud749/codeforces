import sys
sys.setrecursionlimit(100005)

def dfs(v,p,d):
    visited[v]=True
    leaf=True
    for i in per[v]:
        if not visited[i]:
            if v==1:
                dfs(i,p/(len(per[v])),d+1)
            else:
                dfs(i,p/(len(per[v])-1),d+1)
            leaf=False
    if leaf:
        res.append(p*d)



n=int(input())
per=[[] for _ in range(n+1)]
visited=[False]*(n+1)

for i in range(n-1):
    x,y=map(int,input().split())
    per[x].append(y)
    per[y].append(x)

res=[]

dfs(1,1,0)

print(sum(res))