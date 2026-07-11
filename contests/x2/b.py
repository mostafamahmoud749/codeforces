n=int(input())
a=list(map(int,input().split()))
q=int(input())

p=[0]*(n+1)
for i in range(1,n+1):
    p[i]=p[i-1]+(a[i-1]**3)

for i in range(q):
    x=list(map(int,input().split()))
    if len(x)==4:
        l=x[1]
        r=x[2]
        j=x[3]
        extra=0
        loss=0
        for i in range(l-1,len(p)):
            if i<r:
                newv=a[i]+j
                loss+=a[i]**3
                extra+=newv**3
                p[i]=p[i]-loss+extra
                a[i]=newv
            else:
                p[i]+=extra-loss
    else:
        t=x[0]
        l=x[1]
        r=x[2]
        print(p[r]-p[l-1])