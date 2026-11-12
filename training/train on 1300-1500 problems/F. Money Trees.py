import sys
input = lambda: sys.stdin.readline().rstrip()  
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

for _ in range(II()):
  n,k=LII()
  a=LII()
  h=LII()

  i=0
  j=0
  res=0
  cur=0

  while i<n:
    if i>0 and h[i-1]%h[i]!=0:
      cur=0
      j=i

    cur+=a[i]
    while cur>k:
      cur-=a[j]
      j+=1

    res=max(res,i-j+1)
    i+=1

  print(res)