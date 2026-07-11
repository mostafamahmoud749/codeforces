from collections import deque
import sys
input = sys.stdin.readline

t=int(input())
for _ in range(t):
    n,s=map(int,input().split())

    a=list(map(int,input().split()))

    adj=[[] for _ in range(n+1)]



    for i in range(n-1):
        x,y=map(int,input().split())
        adj[x].append(y)
        adj[y].append(x)


    res=float("inf")
    l=[float("inf")]*(n+1)
    l[s]=0
    
    out=[]
    q=deque([s])

    while q:
        v=q.popleft()

        for u in adj[v]:
            if l[v]+1<l[u]:
                l[u]=l[v]+1
                q.append(u)

    for i in a:
        
        res=min(res,l[i])
        q=deque([i])
        l[i]=0

        while q:
            v=q.popleft()

            for u in adj[v]:
                if l[v]+1<l[u] and l[v]+1<res:
                    l[u]=l[v]+1
                    q.append(u)
        out.append(res)
    
    print(*out)



    