n=int(input())
a=list(map(int,input().split()))

adj=[[] for _ in range(n+1)]

for i in range(n-1):

    adj[a[i]].append(i+2)

req=[-1]*(n+1)

for i in range(n,0,-1):
    if len(adj[i])==0:
        req[i]=1
    else:
        req[i]=0
        for j in adj[i]:
            req[i]+=req[j]


res=[]
for i in req:
    if i!=-1:
        res.append(i)

res.sort()
print(*res)