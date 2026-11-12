import sys
input = lambda: sys.stdin.readline().rstrip()  
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

for _ in range(II()):
  a=input()

  a=a.split("B")
  Acount=0
  minA=float("inf")

  for i in a:
    minA=min(minA,len(i))
    if len(i)>0:
      Acount+=len(i)

  print(Acount-minA)