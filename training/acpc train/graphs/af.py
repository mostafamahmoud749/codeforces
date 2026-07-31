from collections import deque

k,n,m=map(int,input().split())

a=[[] for _ in range(k)]

for i in range(k):
    input()
    for j in range(n):
        a[i].append(input())

input()
si,sj=map(int,input().split())

# print(a)

visited=[[[False]*m for _ in range(n)] for _ in range(k)]

# print(visited)



q=deque([(0,si-1,sj-1)])
visited[0][si-1][sj-1]=True

dir=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
res=0

while q:
    ck,ci,cj=q.popleft()
    res+=1
    # print(q)
    for u in dir:
        nk=u[0]+ck
        ni=u[1]+ci
        nj=u[2]+cj

        if 0<=nk<=k-1 and 0<=ni<=n-1 and 0<=nj<=m-1 and a[nk][ni][nj]=="." and not visited[nk][ni][nj]:
            visited[nk][ni][nj]=True
            q.append((nk,ni,nj))


# print(visited)
print(res)