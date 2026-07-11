from collections import deque

n=int(input())
a=list(map(int,input().split()))
even=[]
odd=[]

adj=[[] for _ in range(n)]

for i in range(n):
    if i-a[i]>=0:
        adj[i-a[i]].append(i)
    if i+a[i]<=n-1:
        adj[i+a[i]].append(i)

    if a[i]%2==0:
        even.append(i)
    else:
        odd.append(i)

el=[-1]*n
q=deque(even)
res1=[-1]*n
for i in even:
    el[i]=0

while q:
    v=q.popleft()
    if a[v]%2!=0:
        res1[v]=el[v]

    for i in adj[v]:
        if el[i]==-1:
            el[i]=el[v]+1
            q.append(i)

ol=[-1]*n
q=deque(odd)
res2=[-1]*n

for i in odd:
    ol[i]=0

while q:
    v=q.popleft()
    if a[v]%2==0:
        res2[v]=ol[v]
    
    for i in adj[v]:
        if ol[i]==-1:
            ol[i]=ol[v]+1
            q.append(i)

res=[]

for i in range(n):
    if a[i]%2==0:
        res.append(res2[i])
    else:
        res.append(res1[i])

print(*res)