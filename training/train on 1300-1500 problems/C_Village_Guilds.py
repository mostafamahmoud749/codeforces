import sys
sys.setrecursionlimit(200005)

def dfs(v):
    visited[v]=True
    m1=depth[v]
    m2=depth[v]
    res=1
    for i in per[v]:
        if not visited[i]:
            depth[i]=depth[v]+1
            res+=dfs(i)
            
            if maxdepth[i]>m1:
                m2=m1
                m1=maxdepth[i]
            elif maxdepth[i]>m2:
                m2=maxdepth[i]
    
    maxdepth[v]=m1

    if m2>depth[v]:
        res+=m2-depth[v]

    return res



t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    per=[[] for _ in range(n+1)]
    visited=[False]*(n+1)
    depth=[0]*(n+1)
    maxdepth=[0]*(n+1)
    for i in range(n-1):
        per[i+2].append(a[i])
        per[a[i]].append(i+2)
    
    print(dfs(1))