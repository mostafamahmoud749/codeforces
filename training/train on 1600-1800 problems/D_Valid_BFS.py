

n=int(input())
per=[[] for _ in range(n+1)]

for i in range(n-1):
    x,y=map(int,input().split())
    per[x].append(y)
    per[y].append(x)

a=list(map(int,input().split()))
pos=[0]*(n+1)

for i in range(1,n+1):
    pos[a[i-1]]=i-1

chc=[0]*(n+1)
bfs=[1]
q=[1]
visited=[False]*(n+1)
visited[1]=True
indx=0

while indx<len(q):
    x=q[indx]
    indx+=1
    ch=[]
    for i in per[x]:
        if not visited[i]:
            ch.append(i)
            visited[i]=True
    chc[x]=len(ch)
    q+=ch
    bfs+=ch

# print(bfs)
# print(pos)

l=0
r=1
s=True
if a[0]!=1:
    s=False

while l<n and s:
    v=a[l]
    le=chc[v]
    
    st=set(per[v])
    for i in range(le):
        if a[r+i] not in st:
            s=False
            break
    l+=1
    r+=le


print("YES") if s else print("NO")