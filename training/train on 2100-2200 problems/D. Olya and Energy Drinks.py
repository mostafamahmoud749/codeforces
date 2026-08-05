import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()  # strip the trailing newline
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))


n,m,k=LII()
a=[]
for _ in range(n):
    a.append(input())
x1,y1,x2,y2=LII()

l=[[-1]*m for _ in range(n)]
l[x1-1][y1-1]=0
q=deque([(x1-1,y1-1)])
dir=[(1,0),(-1,0),(0,1),(0,-1)]

while q:
    cx,cy=q.popleft()
    for u in dir:
        for ck in range(1,k+1):
            nx,ny=cx+(u[0]*ck),cy+(u[1]*ck)
            if not (0<=nx<=n-1 and 0<=ny<=m-1) or a[nx][ny]=="#" or (l[nx][ny]!=-1 and l[nx][ny]<l[cx][cy]+1):
                break
            if  l[nx][ny]==-1 :
                l[nx][ny]=l[cx][cy]+1
                q.append((nx,ny))

# print(l)
print(l[x2-1][y2-1])