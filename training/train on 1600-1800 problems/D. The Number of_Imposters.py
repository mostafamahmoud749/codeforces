from collections import deque

t=int(input())
for _ in range(t):
    n,mt=map(int,input().split())

    adj=[[] for _ in range(n+1)]
    m={}

    

    for i in range(mt):
        x,y,s=input().split()
        x=int(x)
        y=int(y)
        if s=="imposter":
            s=0
        else:
            s=1

        adj[x].append((y,s))
        adj[y].append((x,s))
    color=[-1]*(n+1)

    res=0
    for i in range(1,n+1):
        if color[i]==-1:
            c0=0
            c1=0

            
            color[i]=0

            wr=False

            q=deque([i])
            while q:
                v=q.popleft()
                if color[v]==0:
                    c0+=1
                else:
                    c1+=1

                for u,s in adj[v]:
                    pc=-1

                    if color[v]==0:
                        pc=1-s
                    else:
                        pc=s

                    if color[u]==-1:
                        color[u]=pc
                        q.append(u)
                    elif color[u]!=-1 and pc!=color[u]:
                        wr=True
                        break
            if not wr:
                res+=max(c0,c1)

                if wr:
                    break
        if wr:
            break

    
    if wr:
        print(-1)
    else:
        print(res)
