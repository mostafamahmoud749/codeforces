import sys
sys.setrecursionlimit(4005)

def dfs(i):
    global res

    if a[i-1]=="W":
        cres=1
    else:
        cres=-1

    for u in adj[i]:
        if not visited[u]:
            visited[u]=True
            cres+=dfs(u)
            

    if cres==0:
        res+=1

    return cres


t=int(input())
for _ in range(t):
    n=int(input())
    b=list(map(int,input().split()))
    a=input()

    adj=[[] for _ in range(n+1)]
    visited=[False]*(n+1)

    for i in range(n-1):
        adj[b[i]].append(i+2)
        adj[i+2].append(b[i])

    res=0
    visited[1]=True
    dfs(1)
    

    print(res)