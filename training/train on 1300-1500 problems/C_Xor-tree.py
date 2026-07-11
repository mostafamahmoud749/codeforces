from collections import deque

n=int(input())

adj=[[] for _ in range(n+1)]
visited=[False]*(n+1)
l=[-1]*(n+1)
l[1]=0

for i in range(n-1):
    x,y=map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)

value=list(map(int,input().split()))
goal=list(map(int,input().split()))

q=deque([[1,0,0]])
visited[1]=True

res=[]

while q:
    x=q.popleft()
    v=x[0]
    o=x[1]
    e=x[2]

    curv=value[v-1]

    if l[v]%2!=0:
        curv^=e
    else:
        curv^=o

    if curv!=goal[v-1]:
        res.append(v)
        if l[v]%2!=0:
            e=1-e
        else:
            o=1-o
    
    for i in adj[v]:
        if not visited[i]:
            l[i]=l[v]+1
            visited[i]=True
            q.append([i,o,e])

print(len(res))
for i in range(len(res)-1,-1,-1):
    print(res[i])