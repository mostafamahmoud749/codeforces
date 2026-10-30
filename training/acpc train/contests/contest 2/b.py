import sys
import math
input = lambda: sys.stdin.readline().rstrip()  
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

def solve(a,ck,s,indx):
  global res
  if ck==k or indx>=len(div):
    if s==n and ck==k:
      res=a
    return

  if res!=[]: return

  solve(a+[div[indx]],ck+1,s*div[indx],indx)
  solve(a+[div[indx]],ck+1,s*div[indx],indx+1)
  newa=a.copy()
  solve(newa,ck,s,indx+1)


  



n,k=LII()
div=[]

for i in range(2,int(math.sqrt(n))+1):
  if n%i==0:
    div.append(i)
    if (n/i)!=i:
      div.append(n//i)
res=[]


solve([],0,1,0)

print(*res) if res!=[] else print(-1)
