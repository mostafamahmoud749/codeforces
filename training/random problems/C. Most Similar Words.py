import sys
input = lambda: sys.stdin.readline().rstrip()  
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

t=II()

for _ in range(t):
  n,m=LII()

  a=[]
  for i in range(n):
    a.append(input())

  res=float("inf")
  for i in range(n):
    for j in range(i+1,n):
      cur=0
      for c in range(m):
        cur+=abs(ord(a[i][c])-ord(a[j][c]))
      res=min(res,cur)

  print(res)