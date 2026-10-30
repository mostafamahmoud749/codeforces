import sys
input = lambda: sys.stdin.readline().rstrip()  
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

def sieve(n):
  global d
  for i in range(2,int(math.sqrt(n))+1):
    if (d[i]):
      for j in range(i*i,n+1,i):
        d[j]=False