from collections import deque

n,m=map(int,input().split())
h=input()
v=input()

s=True

for ci in range(n):
    for cj in range(m):
        c=0
        visited=[[False]*m for _ in range(n)]
        q=deque([(ci,cj)])
        visited[ci][cj]=True

        while q:
            i,j=q.popleft()
            c+=1
            if h[i]==">":
                nj=j+1
            elif h[i]=="<":
                nj=j-1

            if 0<=nj<=m-1 and not visited[i][nj]:
                visited[i][nj]=True
                q.append((i,nj))

            if v[j]=="v":
                ni=i+1
            elif v[j]=="^":
                ni=i-1

            if 0<=ni<=n-1 and not visited[ni][j]:
                visited[ni][j]=True
                q.append((ni,j))

        if c<n*m:
            s=False
            break
    if not s:
        break

print("YES") if s else print("NO")