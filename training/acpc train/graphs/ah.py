from collections import deque


n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append(list(input().strip()))

adj=[[] for _ in range(n+1)]

c=0
visited=[[False]*m for _ in range(n)]
comps=[[0]*m for _ in range(n)]
b={0:0}

dir=[(1,0),(-1,0),(0,1),(0,-1)]

for i in range(n):
    for j in range(m):
        if not visited[i][j] and a[i][j]!="*":
            c+=1
            size=0
            q=deque([(i,j)])
            visited[i][j]=True
            path=[]

            while q:
                ci,cj=q.popleft()
                size+=1
                path.append((ci,cj))

                for u in dir:
                    ni=ci+u[0]
                    nj=cj+u[1]
                    if 0<=ni<=n-1 and 0<=nj<=m-1 and not visited[ni][nj] and a[ni][nj]!="*":
                        visited[ni][nj]=True
                        q.append((ni,nj))

            for u in path:
                comps[u[0]][u[1]]=c
            b[c]=size

for i in range(n):
    for j in range(m):
        if a[i][j]=="*":
            st=set()
            cres=1
            for u in dir:
                ni=i+u[0]
                nj=j+u[1]
                if 0<=ni<=n-1 and 0<=nj<=m-1:
                    st.add(comps[ni][nj])
            for k in st:
                cres+=b[k]
            a[i][j]=str(cres%10)

for i in a:
    print("".join(i))