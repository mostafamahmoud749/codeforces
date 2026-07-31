from collections import deque

n,m,k=map(int,input().split())

dirc=[(1,0),(-1,0),(0,1),(0,-1)]

a=[]
visited=[[False]*(m) for _ in range(n)]

for _ in range(n):
    a.append(list(input().strip()))

b=[]

for i in range(n):
    for j in range(m):
        if a[i][j]=="." and not visited[i][j]:

            pairs=[]
            imp=False
            q=deque([[i,j]])
            visited[i][j]=True
            cnt=0

            while q:
                ci,cj=q.popleft()

                pairs.append((ci,cj))
                cnt+=1
                if ci==0 or ci==n-1 or cj==0 or cj==m-1:
                    imp=True

                for x,y in dirc:
                    if 0<=ci+x<n and 0<=cj+y<m and a[ci+x][cj+y]=="." and not visited[ci+x][cj+y]:
                        visited[ci+x][cj+y]=True
                        q.append([ci+x,cj+y])
            
            if not imp:
                b.append([cnt,pairs])

b.sort()

cnt=0
for i in range(len(b)-k-1,-1,-1):
    cnt+=b[i][0]
    for x,y in b[i][1]:
        a[x][y]="*"

print(cnt)
for i in a:
    print("".join(i))