import sys
from random import getrandbits
input = sys.stdin.readline
R = getrandbits(32)

n,x=map(int,input().split())
a=list(map(int,input().split()))
db={0^R:1}
p=[0]*(n+1)
res=0
for i in range(1,n+1):
    p[i]=p[i-1]+a[i-1]
    t=(p[i]-x)^R
    if t in db:
        res+=db[t]
        
    curr = p[i] ^ R
    db[curr]=db.get(curr,0)+1
print(res)