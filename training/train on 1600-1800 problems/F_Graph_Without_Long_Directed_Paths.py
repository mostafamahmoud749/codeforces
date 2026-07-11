from collections import deque

n,m=map(int,input().split())
adj=[[] for _ in range(n+1)]
visited=[False]*(n+1)
l=[-1]*(n+1)
l[1]=0
visited[1]=True
e=[]
for _ in range(m):
    x,y=map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)
    e.append([x,y])

q=deque([[1,-1]])
res=[]
s=True

while q and s:
    ele=q.popleft()
    v=ele[0]
    p=ele[1]
    
    for i in adj[v]:
        if i!=p and visited[i]:
            if l[i]%2==l[v]%2:
                s=False
                break
        if not visited[i]:
            l[i]=l[v]+1
            visited[i]=True
            q.append([i,v])

if s:
    for i in e:
        if l[i[0]]%2==0:
            res.append("1")
        else:
            res.append("0")
    print("YES")
    print("".join(res))
else:
    print("NO")
