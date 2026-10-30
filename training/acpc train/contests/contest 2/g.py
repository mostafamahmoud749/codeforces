import sys
import math
input = lambda: sys.stdin.readline().rstrip()  
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))




n=II()
res=[]
freq=0

for i in range(1,1001):
  for j in range(i+1,1001):
    if (i/j!=i//j) and math.gcd(i,j)==1 and i+j==n and ((i/j)%1>freq):
      freq=(i/j)%1
      res=[i,j]


print(res[0],res[1])
