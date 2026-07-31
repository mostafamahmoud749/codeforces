from collections import deque

n,m=map(int,input().split())
n1,n2,n3=map(int,input().split())
t1=n1+n3
t2=n2

adj=[[] for _ in range(n+1)]

for i in range(m):
    x,y=map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)

color=[-1]*(n+1)

if t1>=t2:
    t1=-1
    q=deque([1])
    color[1]=0
else:
    t2=-1
    q=deque([1])
    color[1]=1

while q:
    v=q.popleft()
    for i in adj[v]:
        if color[i]==-1:
            q.append(i)
            color[i]=1-color[v]
            
            if color[i]==0:
                t1-=1
            else:
                t2-=1

print(t1,t2)
print(color)

if t1<0 or t2<0:
    print("NO")
else:
    print("YES")
