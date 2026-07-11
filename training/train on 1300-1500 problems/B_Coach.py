def dfs(v):
    global r,cur
    visited[v]=True
    cur.append(v)
    for i in per[v]:
        if not visited[i]:
            dfs(i)



n,m=map(int,input().split())
visited=[False]*(n+1)
per=[[] for _ in range(n+1)]

for i in range(m):
    x,y=map(int,input().split())
    per[x].append(y)
    per[y].append(x)

t1=[]
t2=[]
t3=[]
r=False
cur=[]

for i in range(1,n+1):
    if not visited[i]:
        cur=[]
        dfs(i)
        
        if len(cur)>3:
            r=True
        else:
            if len(cur)==3:
                t3.append(cur)
            elif len(cur)==2:
                t2.append(cur)
            else:
                t1.append(cur)
    if r:
        break

if r or len(t1)<len(t2):
    print(-1)
else:
    for i in t3:
        print(*i)
    for i in range(len(t2)):
        print(*t2[i],*t1[i])
    for i in range(len(t2),len(t1),3):
        print(*t1[i],*t1[i+1],*t1[i+2])
