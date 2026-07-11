import sys
sys.setrecursionlimit(150005)

def dfs(v,ec):
    global vc,cs
    visited[v]=True
    vc+=1
    if ec!=len(per[v]) or not cs:
        cs=False
        return
    for i in per[v]:
        if not visited[i]:
            dfs(i,ec)

n,m=map(int,input().split())
visited=[False]*(n+1)
per=[[] for _ in range(n+1)]

for i in range(m):
    x,y=map(int,input().split())
    per[x].append(y)
    per[y].append(x)

s=True

for i in range(1,n+1):
    if not visited[i]:
        vc=0
        ec=len(per[i])
        cs=True
        dfs(i,ec)

        # print(vc,ec,cs)
        if vc-1!=ec or not cs:
            s=False
            break


print("YES") if s else print("NO")
