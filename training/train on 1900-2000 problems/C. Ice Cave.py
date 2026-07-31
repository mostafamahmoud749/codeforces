from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()  # strip the trailing newline
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))


n,m=LII()
a=[]
for _ in range(n):
    a.append(input())

si,sj=LII()
ti,tj=LII()
si,sj=si-1,sj-1
ti,tj=ti-1,tj-1


dir=[(1,0),(-1,0),(0,1),(0,-1)]

s=False
c=0
for u in dir:
    ni,nj=ti+u[0],tj+u[1]
    if 0<=ni<=n-1 and 0<=nj<=m-1 and (a[ni][nj]=="." or (ni==si and nj==sj)):
        c+=1

if a[ti][tj]=="." and c>=2:
    s=True
elif a[ti][tj]=="X" and c>=1:
    s=True

if not s:
    print("NO")
    exit()

visited=[[False]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if a[i][j]=="X":
            visited[i][j]=True

q=deque([(ti,tj)])
visited[ti][tj]=True
visited[si][sj]=False

while q:
    ci,cj=q.popleft()
    for u in dir:
        ni,nj=ci+u[0],cj+u[1]
        if 0<=ni<=n-1 and 0<=nj<=m-1 and not visited[ni][nj]:
            visited[ni][nj]=True
            q.append((ni,nj))

if visited[si][sj]:
    print("YES")
else:
    print("NO")