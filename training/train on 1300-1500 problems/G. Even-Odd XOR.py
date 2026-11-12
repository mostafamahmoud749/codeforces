import sys
input = lambda: sys.stdin.readline().rstrip()  
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

for _ in range(II()):
  n=II()

  a=[]
  x1=0
  for i in range(n-3):
    x1^=i
    a.append(i)

  x2=1<<29
  x3=1<<30

  x4=x1^x2^x3

  print(*a,x2,x3,x4)
