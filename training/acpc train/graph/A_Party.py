import sys
sys.setrecursionlimit(3000)

res=0
def dfs(u,depth):
    global res
    visted[u]=1
    depth+=1
    res=max(res,depth)
    for v in ver[u]:
        if visted[v]==0:
            dfs(v,depth)
n=int(input())
ver=[[] for i in range(n)]
visted=[0]*n
roots=[]
for i in range(n):
    u=int(input())
    if u==-1:
        roots.append(i)
    else:
        ver[u-1].append(i)
for r in roots:
    dfs(r,0)
print(res)