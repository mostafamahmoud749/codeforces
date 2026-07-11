from collections import deque

t=int(input())
for _ in range(t):
    n,m=map(int,input().split())

    adj=[[] for _ in range(n+1)]
    color=[-1]*(n+1)
    color[1]=0

    for i in range(m):
        x,y=map(int,input().split())
        adj[x].append(y)
        adj[y].append(x)

    c0=[]
    c1=[]

    q=deque([1])

    while q:
        v=q.popleft()
        
        for i in adj[v]:
            if color[i]==-1:
                color[i]=1-color[v]
                q.append(i)
    
    for i in range(1,n+1):
        if color[i]==1:
            c1.append(i)
        else:
            c0.append(i)
    
    if len(c1)<len(c0):
        print(len(c1))
        print(*c1)
    else:
        print(len(c0))
        print(*c0)
