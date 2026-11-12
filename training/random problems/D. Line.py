import sys
input = lambda: sys.stdin.readline().rstrip()  
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

for _ in range(II()):
  n=II()
  a=input()

  diff=[]

  s=0
  for i in range(n):
    l=i
    r=n-i-1

    if a[i]=="L":
      s+=l
      diff.append(r-l)
    else:
      s+=r
      diff.append(l-r)

  diff.sort()
  diff=diff[::-1]

  res=[]
  for i in range(n):
    if diff[i]>0:
      s+=diff[i]
    res.append(s)

  print(*res)