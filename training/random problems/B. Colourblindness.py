import sys
input = lambda: sys.stdin.readline().rstrip()  
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

for _ in range(II()):
  n=II()
  a=input()
  b=input()
  s=True

  for i in range(n):
    if (a[i]=="R" and b[i]!="R") or (a[i]!="R" and b[i]=="R"):
      s=False

  print("YES") if s else print("NO")