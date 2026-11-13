import sys
input = lambda: sys.stdin.readline().rstrip()  
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

for _ in range(II()):
  a=LII()
  a.sort()

  if a[1]-a[0]==1 and a[2]-a[1]==1:
    print("YES")
  else:
    print("NO")