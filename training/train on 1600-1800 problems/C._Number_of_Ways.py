n=int(input())
a=list(map(int,input().split()))
s=sum(a)
if s%3!=0:
    print(0)
else:
    t=s//3
    res=0
    c_t=0
    s=0
    for i in range(n - 1):
        s+=a[i]
        if s==2*t:
            res+=c_t
        if s==t:
            c_t+=1
    print(res)