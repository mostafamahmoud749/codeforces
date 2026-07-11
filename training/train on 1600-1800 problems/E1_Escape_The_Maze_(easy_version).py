from collections import deque

t=int(input())
for _ in range(t):
    input()
    n,k=map(int,input().split())

    frinds=list(map(int,input().split()))

    adj=[[] for _ in range(n+1)]

    for _ in range(n-1):
        x,y=map(int,input().split())
        adj[x].append(y)
        adj[y].append(x)

    q=deque(frinds)
    l1=[-1]*(n+1)
    for i in frinds:
        l1[i]=0

    while q:
        v=q.popleft()
        for u in adj[v]:
            if l1[u]==-1:
                l1[u]=l1[v]+1
                q.append(u)


    l2=[-1]*(n+1)
    l2[1]=0

    q=deque([1])
    while q:
        v=q.popleft()
        for u in adj[v]:
            if l2[u]==-1:
                l2[u]=l2[v]+1
                q.append(u)

    s=False
    for i in range(1,n+1):
        if (i!=1 and len(adj[i])==1) or (i==1 and len(adj[i])==0):
            if l2[i]!=-1 and (l1[i]==-1 or l2[i]<l1[i]):
                s=True
                break
    
    print("YES") if s else print("NO")


