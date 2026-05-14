import sys
sys.setrecursionlimit(200000)

def dfs(u,c):
    global res
    curcats=c
    if a[u]==1:
        curcats+=1
    else: curcats=0
    visted[u]=1
    if curcats<=m:
        is_l=True
        for v in ver[u]:
            if visted[v]==0:
                is_l=False
                dfs(v,curcats)
        if is_l:
            res+=1

n,m=map(int,input().split())
a=list(map(int,input().split()))
ver=[[] for _ in range(n)]
visted=[0]*n
res=0
for i in range(n-1):
    u,v=map(int,input().split())
    ver[u-1].append(v-1)
    ver[v-1].append(u-1)
dfs(0,0)
print(res)