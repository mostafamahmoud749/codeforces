from collections import deque

n,m,x=map(int,input().split())

a=[]

for i in range(n):
    a.append(list(input().strip()))

visited=[[False] * m for _ in range(n)]
res=[[-1] * m for _ in range(n)]

for _ in range(x):
    i,j=map(int,input().split())
    
    i-=1
    j-=1

    if res[i][j]!=-1:
        print(res[i][j])
        continue

    q=deque([[i,j]])
    visited[i][j]=True
    cres=0
    path=[[i,j]]


    while q:
        i,j=q.popleft()
        if i<n-1 and a[i+1][j]=="*":
            cres+=1
        if i>0 and a[i-1][j]=="*":
            cres+=1
        if j<m-1 and a[i][j+1]=="*":
            cres+=1
        if j>0 and a[i][j-1]=="*":
            cres+=1


        if i<n-1 and a[i+1][j]=="." and not visited[i+1][j]:
            q.append([i+1,j])
            visited[i+1][j]=True
            path.append([i+1,j])

        if i>0 and a[i-1][j]=="." and not visited[i-1][j]:
            q.append([i-1,j])
            visited[i-1][j]=True
            path.append([i-1,j])

        if j<m-1 and a[i][j+1]=="." and not visited[i][j+1]:
            q.append([i,j+1])
            visited[i][j+1]=True
            path.append([i,j+1])

        if j>0 and a[i][j-1]=="." and not visited[i][j-1]:
            q.append([i,j-1])
            visited[i][j-1]=True
            path.append([i,j-1])
    
    for i,j in path:
        res[i][j]=cres
    print(cres)



