import sys
sys.setrecursionlimit(200005)


def dfs(v,l,p):
    for x,indx in per[v]:
        if x!=p:
            res[indx]=7-l
            dfs(x,7-l,v)


t=int(input())
for _ in range(t):
    n=int(input())
    per=[[] for _ in range(n+1)]

    for i in range(n-1):
        x,y=map(int,input().split())
        per[x].append([y,i])
        per[y].append([x,i])
    
    s=True
    start=0
    for i in range(1,n+1):
        if len(per[i])>2:
            s=False
            break
        if len(per[i])==1:
            start=i

    if not s:
        print(-1)
        continue

    res=[0]*(n-1)
    dfs(start,5,-1)

    print(*res)
