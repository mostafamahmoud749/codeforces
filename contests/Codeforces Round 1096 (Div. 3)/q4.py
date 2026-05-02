import math
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    f0=-1
    s0=-1
    for i in range(len(a)):
        if a[i]==0 and f0==-1:
            f0=i
        elif a[i]==0 and s0==-1:
            s0=i
    s=True
    i=s0
    j=f0
    while j<=i:
        if a[i]!=a[j]:
            s=False
            break
        else:
            i-=1
            j+=1
    if s==False:
        print(0)
    else:
        it=min(f0,(n*2)-s0-1)
        i=s0
        j=f0
        while it>0:
            if a[j-1]==a[i+1]:
                i+=1
                j-=1
            else:
                break
            it-=1
        s=set(a[j:i+1])
        print(a[j:i+1])
        c1=0
        while c1 in s:
            c1+=1
        print(c1)