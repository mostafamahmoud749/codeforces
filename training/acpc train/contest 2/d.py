n=int(input())
a=list(map(int,input().split()))
m=int(input())
s_a=a.copy()
s_a.sort()
p=[0]*(n+1)
sp=[0]*(n+1)
for i in range(1,n+1):
    p[i]=p[i-1]+a[i-1]
for i in range(1,n+1):
    sp[i]=sp[i-1]+s_a[i-1]
for i in range(m):
    q,l,r=map(int,input().split())
    if q == 1:
        print(p[r]-p[l-1])
    else:
        print(sp[r]-sp[l-1])