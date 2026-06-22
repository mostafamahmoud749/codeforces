n=int(input())
a=list(map(int,input().split()))
res=0
i=0
j=0
oldindx=0
used=1
old=0
while i<n-1:
    i+=1
    if a[i]<=a[i-1] and used==1:
        old=a[i]
        oldindx=i
        used=0
        a[i]=a[i-1]+1
    elif a[i]<=a[i-1]:
        a[oldindx]=old
        j=oldindx
        used=1
    res=max(res,i-j+1)
print(res)
