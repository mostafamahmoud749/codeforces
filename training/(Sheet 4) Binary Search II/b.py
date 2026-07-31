def ask(mid):
    print("?",mid,mid)
    res=int(input())
    return mid*mid!=res 

t=int(input())
for _ in range(t):
    l=2
    r=999
    res=-1
    while l<=r:
        mid=l+(r-l)//2
        if ask(mid):
            res=mid
            r=mid-1
        else:
            l=mid+1
    print("!",res)