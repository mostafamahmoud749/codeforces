import sys
input = lambda: sys.stdin.readline().rstrip()  
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

t=II()

for _ in range(t):
  n,m=LII()

  a=[]
  for i in range(n):
    a.append(LII())

  dir=[(1,1),(-1,1),(1,-1),(-1,-1)]
  res=float("-inf")
  for i in range(n):
    for j in range(m):
      cur=a[i][j]
      for r in range(1,max(n,m)+1):
        for u in dir:
          ci=i+(u[0]*r)
          cj=j+(u[1]*r)

          if 0<=ci<n and 0<=cj<m:
            cur+=a[ci][cj]
      res=max(res,cur)

  print(res)