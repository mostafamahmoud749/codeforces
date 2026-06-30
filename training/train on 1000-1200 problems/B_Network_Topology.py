n,m=map(int,input().split())

freq=[0]*(n+1)

for i in range(m):
    x,y=map(int,input().split())
    freq[x]+=1
    freq[y]+=1


star=False
c1=0
c2=0

for i in range(1,n+1):
    if freq[i]==1:
        c1+=1
    if freq[i]==2:
        c2+=1
    if freq[i]==n-1:
        star=True

if star and c1==n-1 and n==m+1:
    print("star topology")
elif c1==2 and c2==n-2 and n==m+1:
    print("bus topology")
elif  c2==n and n==m:
    print("ring topology")
else:
    print("unknown topology")



