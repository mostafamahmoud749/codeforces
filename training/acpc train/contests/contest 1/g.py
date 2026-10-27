import sys
import math
input = lambda: sys.stdin.readline().rstrip()  
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

def solve(mid):
  cur=mid
  curc=1
  for i in range(0,n-1):
    if (a[i]==a[i+1]): 
      curc+=1
    else:
      cur-=(curc//2)
      curc=1

  if curc>1:
    cur-=(curc//2)


  if (cur>=0):
    return True
  return False
  


n=II()
a=LII()

l=0
r=n+1
res=-1

while (l<=r):
  mid=l+(r-l)//2
  if (solve(mid)):
    res=mid
    r=mid-1
  else:
    l=mid+1

print(res)
