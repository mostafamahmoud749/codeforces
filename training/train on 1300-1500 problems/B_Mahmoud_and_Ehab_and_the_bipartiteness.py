from collections import deque

n=int(input())


adj=[[] for _ in range(n+1)]

for i in range(n-1):
    x,y=map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)

q=deque([1])
teams=[-1]*(n+1)
teams[1]=0

while q:
    v=q.popleft()

    for i in adj[v]:
        if teams[i]==-1:
            q.append(i)
            teams[i]=1-teams[v]

c0=0
c1=0

for i in range(1,n+1):
    if teams[i]==0:
        c0+=1
    else:
        c1+=1

print((c0*c1)-(n-1))