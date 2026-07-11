from collections import deque

t=int(input())
for _ in range(t):
    input()
    n,k=map(int,input().split())

    leafs=[]

    adj=[[] for _ in range(n+1)]
    l=[-1]*(n+1)

    lf=[0]*(n+1)
    has=-1

    for i in range(n-1):
        x,y=map(int,input().split())
        adj[x].append(y)
        adj[y].append(x)
    
    q=deque([])

    for i in range(1,n+1):
        if len(adj[i])==1:
            leafs.append(i)
            q.append(i)
            l[i]=0

    while q:
        v=q.popleft()
        lf[l[v]]+=1
        has=max(has,l[v])
        for i in adj[v]:
            if l[i]==-1:
                l[i]=l[v]+1
                q.append(i)
    

    print(sum(lf[k:has+1]))

    