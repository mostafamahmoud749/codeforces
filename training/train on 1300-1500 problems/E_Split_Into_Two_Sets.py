from collections import deque

t=int(input())
for _ in range(t):
    maxv=-1
    m=int(input())
    inp=[]
    s=True

    for i in range(m):
        x,y=map(int,input().split())
        if x==y:
            s=False

        maxv=max(maxv,x,y)
        inp.append([x,y])
    
    if not s:
        print("NO")
        continue

    freq=[0]*(maxv+1)

    for i in inp:
        freq[i[0]]+=1
        freq[i[1]]+=1
        if freq[i[0]]>2 or freq[i[1]]>2:
            s=False
            break
    
    if not s:
        print("NO")
        continue

    adj=[[] for _ in range(maxv+1)]
    visited=[False]*(maxv+1)

    for i in inp:
        adj[i[0]].append(i[1])
        adj[i[1]].append(i[0])



    for i in range(1,maxv+1):
        if not visited[i]:
            q=deque([i])
            visited[i]=True
            l=0
            while q:
                l+=1
                v=q.popleft()
                for u in adj[v]:
                    if not visited[u]:
                        visited[u]=True
                        q.append(u)
            if l%2!=0:
                s=False
                break

    print("YES") if s else print("NO")