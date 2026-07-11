from collections import deque

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))

    adj=[set() for _ in range(n+1)]

    for i in range(n):
        adj[i+1].add(a[i])
        adj[a[i]].add(i+1)

    visited=[False]*(n+1)


    comps=0
    cycComps=0

    for i in range(1,n+1):
        if not visited[i]:
            c=[]
            q=deque([i])
            visited[i]=True
            cyc=True

            while q:
                v=q.popleft()
                c.append(v)
                for u in adj[v]:
                    if visited[u]:
                        cyc=True
                    else:
                        visited[u]=True
                        q.append(u)
            for v in c:
                if len(adj[v])<2:
                    cyc=False
                    break

            if cyc:
                cycComps+=1
            else:
                comps+=1
    
    if comps>0:
        print(cycComps+1,cycComps+comps)
    else:
        print(cycComps,cycComps+comps)


