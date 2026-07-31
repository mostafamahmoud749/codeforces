from collections import deque

n,m=map(int,input().split())
a=[]
for _ in range(n):
    a.append(input())

one=[]
two=[]
three=[]

for i in range(n):
    for j in range(m):
        if a[i][j]=="1":
            one.append((i,j))
        elif a[i][j]=="2":
            two.append((i,j))
        elif a[i][j]=="3":
            three.append((i,j))

q=deque([])
l1=[[float("inf")]*m for _ in range(n)]

for i,j in one:
    l1[i][j]=0
    q.append((i,j))

dir=[(1,0),(-1,0),(0,1),(0,-1)]

while q:
    ci,cj=q.popleft()
    for u in dir:
        ni=ci+u[0]
        nj=cj+u[1]
        

        if 0<=ni<=n-1 and 0<=nj<=m-1 and a[ni][nj]!="#":
            cost=1 if a[ni][nj]=="." else 0

            if l1[ci][cj]+cost<l1[ni][nj]:
                
                l1[ni][nj]=l1[ci][cj]+cost

                if a[ni][nj]==".":
                    q.append((ni,nj))
                else:
                    q.appendleft((ni,nj))

l2=[[float("inf")]*m for _ in range(n)]

for i,j in two:
    l2[i][j]=0
    q.append((i,j))

dir=[(1,0),(-1,0),(0,1),(0,-1)]

while q:
    ci,cj=q.popleft()
    for u in dir:
        ni=ci+u[0]
        nj=cj+u[1]
        

        if 0<=ni<=n-1 and 0<=nj<=m-1 and a[ni][nj]!="#":
            cost=1 if a[ni][nj]=="." else 0

            if l2[ci][cj]+cost<l2[ni][nj]:
                
                l2[ni][nj]=l2[ci][cj]+cost
                
                if a[ni][nj]==".":
                    q.append((ni,nj))
                else:
                    q.appendleft((ni,nj))

l3=[[float("inf")]*m for _ in range(n)]

for i,j in three:
    l3[i][j]=0
    q.append((i,j))

dir=[(1,0),(-1,0),(0,1),(0,-1)]

while q:
    ci,cj=q.popleft()
    for u in dir:
        ni=ci+u[0]
        nj=cj+u[1]
        

        if 0<=ni<=n-1 and 0<=nj<=m-1 and a[ni][nj]!="#":
            cost=1 if a[ni][nj]=="." else 0

            if l3[ci][cj]+cost<l3[ni][nj]:
                
                l3[ni][nj]=l3[ci][cj]+cost
                
                if a[ni][nj]==".":
                    q.append((ni,nj))
                else:
                    q.appendleft((ni,nj))

res=float("inf")

for i in range(n):
    for j in range(m):
        cur=l1[i][j]+l2[i][j]+l3[i][j]
        if cur<float("inf"):
            s=2 if a[i][j]=="." else 0
            res=min(res,cur-s)

print(res) if res!=float("inf") else print(-1)