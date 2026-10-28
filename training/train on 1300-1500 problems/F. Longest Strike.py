import sys
input = lambda: sys.stdin.readline().rstrip()  
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

t=II()

for _ in range(t):
  n,k=LII()

  a=LII()

  a.sort()

  v=[]
  i=0
  while i<n:
    j=i+1
    while j<n and a[i]==a[j]:
      j+=1

    if j-i>=k:
      v.append(a[i])
    i=j

  if not v:
    print(-1)
    continue

  lres=0
  rres=0
  c=0
  l=0
  for r in range(1,len(v)+1):
    if r==len(v) or v[r]!=v[r-1]+1:
      if r-l>c:
        lres=v[l]
        rres=v[r-1]
        c=r-l
      l=r



  print(lres,rres)

