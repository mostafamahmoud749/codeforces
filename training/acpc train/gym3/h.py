from collections import deque
import sys

input=sys.stdin.readline
neg=-10**18


def best_k(a,k):
    b=[]
    for x in a:
        if x[0]==neg:
            continue
        i=0
        while i<len(b) and b[i][0]>=x[0]:
            i+=1
        b.insert(i,x)
        if len(b)>k:
            b.pop()
    return b


n=int(input())

adj=[[] for _ in range(n+1)]

for _ in range(n-1):
    x,y=map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)


parent=[0]*(n+1)
order=[1]
for v in order:
    for u in adj[v]:
        if u!=parent[v]:
            parent[u]=v
            order.append(u)


d1=[neg]*(n+1)
e1=[0]*(n+1)
d2=[neg]*(n+1)
e2=[0]*(n+1)

for v in reversed(order):
    c=[(0,v,0)]
    for u in adj[v]:
        if u==parent[v]:
            continue
        if d1[u]!=neg:
            c.append((d1[u]+1,e1[u],u))
        if d2[u]!=neg:
            c.append((d2[u]+1,e2[u],u))
    b=best_k(c,2)
    d1[v],e1[v]=b[0][0],b[0][1]
    if len(b)>1:
        d2[v],e2[v]=b[1][0],b[1][1]


u1=[neg]*(n+1)
v1=[0]*(n+1)
u2=[neg]*(n+1)
v2=[0]*(n+1)

ans=-1
ah=1
aa=1
ab=2

for v in order:
    c=[(0,v,0)]
    if u1[v]!=neg:
        c.append((u1[v],v1[v],-1))
    if u2[v]!=neg:
        c.append((u2[v],v2[v],-1))
    for u in adj[v]:
        if u==parent[v]:
            continue
        if d1[u]!=neg:
            c.append((d1[u]+1,e1[u],u))
        if d2[u]!=neg:
            c.append((d2[u]+1,e2[u],u))

    b=best_k(c,4)

    t=[]
    for x in b:
        if x[2]!=0:
            t.append(x)
        if len(t)==2:
            break
    if len(t)==2 and t[0][0]+t[1][0]>ans:
        ans=t[0][0]+t[1][0]
        ah=v
        aa=t[0][1]
        ab=t[1][1]

    for u in adj[v]:
        if u==parent[v]:
            continue
        t=[]
        for x in b:
            if x[2]!=u:
                t.append(x)
            if len(t)==2:
                break
        if len(t)==0:
            continue
        u1[u]=t[0][0]+1
        v1[u]=t[0][1]
        if len(t)>1:
            u2[u]=t[1][0]+1
            v2[u]=t[1][1]
        else:
            u2[u]=neg


print(ah)
print(aa,ab)
