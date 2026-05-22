import math

def check(t1,t2,indx):
    global res
    if indx==10 or t1>t2+math.ceil((10-indx)/2) or t2>t1+((10-indx)//2):
        res=min(res,indx)
        return
    if indx%2==0:
        if s[indx]!="?":
            t1+=int(s[indx])
            check(t1,t2,indx+1)
        else:
            check(t1+1,t2,indx+1)
            check(t1,t2,indx+1)
    else:
        if s[indx]!="?":
            t2+=int(s[indx])
            check(t1,t2,indx+1)
        else:
            check(t1,t2+1,indx+1)
            check(t1,t2,indx+1)

t=int(input())
for _ in range(t):
    s=input()
    res=10
    check(0,0,0)
    print(res)