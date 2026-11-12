import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()  
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

for _ in range(II()):
  n,m=LII()

  a=[]
  for i in range(n):
    a.append(input())

  visited=[[False] * m for _ in range(n)]

  dir=[(1,1),(-1,-1),(1,-1),(-1,1),(1,0),(-1,0),(0,1),(0,-1)]

  s=True

  for i in range(n):
    for j in range(m):
      if not visited[i][j] and a[i][j]=="*":
        path=[]
        visited[i][j]=True
        q=deque([(i,j)])

        while q:
          ci,cj=q.popleft()

          path.append((ci,cj))
          for u in dir:
            ni=ci+u[0]
            nj=cj+u[1]

            if 0<=ni<n and 0<=nj<m and not visited[ni][nj] and a[ni][nj]=="*":
              visited[ni][nj]=True
              q.append((ni,nj))

        if len(path)!=3:
          s=False
        else:
          x1,y1=path[0]
          x2,y2=path[1]
          x3,y3=path[2]

          h=max(x1,x2,x3)-min(x1,x2,x3)
          w=max(y1,y2,y3)-min(y1,y2,y3)

          if h!=1 or w!=1:
            s=False

        if not s:
          break

    if not s:
      break

  print("YES" if s else "NO")

