from collections import deque

n,m=map(int,input().split())

adj=[[] for _ in range(n+1)]


for i in range(m):
    x,y=map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)

s1,t1,l1=map(int,input().split())
s2,t2,l2=map(int,input().split())

tl=[[] for _ in range(n+1)]

for i in range(1,n+1):
    l=[-1]*(n+1)
    l[i]=0
    q=deque([i])

    while q:
        v=q.popleft()
        for u in adj[v]:
            if l[u]==-1:
                l[u]=l[v]+1
                q.append(u)
    tl[i]=l

res=-1

if tl[s1][t1]<=l1 and tl[s2][t2]<=l2:
    res=tl[s1][t1]+tl[s2][t2]

if res!=-1:
    for i in range(1,n+1):
        for j in range(1,n+1):
            d1=tl[s1][i]+tl[i][j]+tl[j][t1]
            d2=tl[s2][i]+tl[i][j]+tl[j][t2]

            if d1<=l1 and d2<=l2:
                res=min(res,d1+d2-tl[i][j])

            d1=tl[s1][i]+tl[i][j]+tl[j][t1]
            d2=tl[s2][j]+tl[i][j]+tl[i][t2]
            
            if d1<=l1 and d2<=l2:
                res=min(res,d1+d2-tl[i][j])


print(m-res) if res!=-1 else print(-1)
