import sys
input = lambda: sys.stdin.readline().rstrip()  
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

n,h=LII()

res=0

turns=2
minus=0


for i in range(n):
  x= min(h,2** max(i,1))
  res+= x*(n-i)
  h-= x
  if h==0:
    break

  
print(res+1)