from collections import deque

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))

    adj=[[] for _ in range(n+1)]

    for i in range(n-1):
        x,y=map(int,input().split())
        adj[x].append(y)
        adj[y].append(x)

    st=set(a)
    start=a[0]

    visited=[False]*(n+1)
    visited[start]=True
    res=-1

    q=deque([start])
    while q:
        v=q.popleft()
        
        if v in st:
            start=v

        for i in adj[v]:
            if not visited[i]:
                q.append(i)
                visited[i]=True
    
    l=0
    visited=[False]*(n+1)
    visited[start]=True

    q=deque([[start,0]])
    while q:
        v,d=q.popleft()
        
        if v in st:
            l=d

        for i in adj[v]:
            if not visited[i]:
                q.append([i,d+1])
                visited[i]=True

    print((l+1)//2)