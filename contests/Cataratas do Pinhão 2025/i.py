n,m,q=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

for i in range(n-m):
    a.append((a[i]+a[i+1])%(3*(10**7)))

a.sort()
for i in range(q):
    print(a[b[i]-1])