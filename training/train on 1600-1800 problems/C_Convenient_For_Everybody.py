n=int(input())
a=list(map(int,input().split()))
s,f=map(int,input().split())
maxcount=0
curcount=0
for i in range(f-s):
    curcount+=a[i]
maxcount=curcount
i=f-s-1
j=0
res=s
for x in range(1,n):
    i=(i+1)%n
    curcount+=a[i]
    curcount-=a[j]
    j=(j+1)%n

    cur=(s-x)%n
    if cur==0:
        cur=n
    
    if curcount>maxcount:
        maxcount=curcount
        res=cur
    elif curcount==maxcount:
        res=min(res,cur)
print(res)
