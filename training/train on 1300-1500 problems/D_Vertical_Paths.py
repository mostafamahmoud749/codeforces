import sys
sys.setrecursionlimit(200005)

def dfs(v):
    global path
    visited[v]=True
    f=True
    path.append(v)
    for i in per[v]:
        if not visited[i]:
            if f:
                f=False
                dfs(i)
            else:
                if path!=[]:
                    res.append(path)
                    path=[]
                dfs(i)

    if f and path!=[]:
        res.append(path)
        path=[]

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    per=[[] for _ in range(n+1)]
    visited=[False]*(n+1)

    root=0
    for i in range(n):
        if i+1==a[i]:
            root=i+1
            continue
        per[i+1].append(a[i])
        per[a[i]].append(i+1)

    path=[]
    res=[]
    dfs(root)
    
    # print(root)
    # print(per)


    print(len(res))
    for i in res:
        print(len(i))
        print(*i)
    print()