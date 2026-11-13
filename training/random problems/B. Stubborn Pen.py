import sys
input = lambda: sys.stdin.readline().rstrip()  
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

for _ in range(II()):
  n=II()
  a=input()
  cur="R"

  res=0
  for i in a:
    if cur!=i:
      res+=1
      cur=i
  
    if cur=="R":
      cur="B"
    else:
      cur="R"

  print(res)