n,q=map(int,input().split())
a=[0]*n
ra=[0]*n
ga=[] 
res=0
p=0
for _ in range(q):
    t,x=map(int,input().split())
    if t==1:
        res+=1
        a[x-1]+=1
        ga.append(x-1)
    elif t==2:
        res-=a[x-1]
        ra[x-1]=len(ga)
        a[x-1]=0
    else:
        while p<x:
            if p>=ra[ga[p]]:
                res-=1
                a[ga[p]]-=1
            p+=1
    print(res)
