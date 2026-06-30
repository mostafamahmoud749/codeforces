n,m=map(int,input().split())

p=[True]*(n+1)
for i in range(m):
    x,y=map(int,input().split())
    p[x]=False
    p[y]=False

x=0
for i in range(1,n+1):
    if p[i]==True:
        x=i
        break

print(n-1)
for i in range(1,n+1):
    if i!=x:
        print(x,i)