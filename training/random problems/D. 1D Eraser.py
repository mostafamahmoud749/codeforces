import sys
input = lambda: sys.stdin.readline().rstrip()  
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

for _ in range(II()):
  n,k=LII()
  a=input()

  res=0
  i=0
  while i<n:
    if a[i]=="B":
      res+=1
      curk=k
      while i<n and curk>0:
        a[i]=="W"
        i+=1
        curk-=1
    else:
      i+=1


  print(res)
