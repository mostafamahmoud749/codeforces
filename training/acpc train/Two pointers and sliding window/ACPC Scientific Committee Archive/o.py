import math
n=int(input())
a=list(map(int,input().split()))
p=[0]*(n+2)
s=[0]*(n+2)
for i in range(1,n+1):
    p[i]=math.gcd(p[i-1],a[i-1])
for i in range(n,0,-1):
    s[i]=math.gcd(s[i+1],a[i-1])
q=int(input())
for i in range(q):
    v=int(input())
    print(math.gcd(p[v-1],s[v+1]))
