from collections import deque


t=int(input())
for _ in range(t):
    n,a,b=map(int,input().split())

    adj=[[] for _ in range(n+1)]
    deg=[0]*(n+1)

    for i in range(n):
        x,y=map(int,input().split())
        adj[x].append(y)
        adj[y].append(x)
        deg[x]+=1
        deg[y]+=1
    
    # get the cyc nodes
    q=deque([])
    for i in range(1,n+1):
        if len(adj[i])==1:
            q.append(i)
    cyc=[True]*(n+1)

    while q:
        v=q.popleft()
        cyc[v]=False
        for i in adj[v]:
            deg[i]-=1
            if deg[i]==1:
                q.append(i)

    cycnodes=[]
    for i in range(1,n+1):
        if cyc[i]:
            cycnodes.append(i)
    

    # calc the d from m to cycnodes

    q=deque([a])

    l1=[-1]*(n+1)
    l1[a]=0

    while q:
        v=q.popleft()
        for i in adj[v]:
            if l1[i]==-1:
                l1[i]=l1[v]+1
                q.append(i)

    # calc the d from v to cycnodes

    q=deque([b])

    l2=[-1]*(n+1)
    l2[b]=0

    while q:
        v=q.popleft()
        for i in adj[v]:
            if l2[i]==-1:
                l2[i]=l2[v]+1
                q.append(i)
    
    s=False

    for i in cycnodes:
        if l1[i]>l2[i]:
            s=True
            break
    
    print("YES") if s else print("NO")
