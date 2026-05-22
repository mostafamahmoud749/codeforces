import bisect

def countav(s,e):
    l=bisect.bisect_left(h,s)
    r=bisect.bisect_right(h,e)
    return r-l

def check(s,e):
    av=countav(s, e)
    if av==0:
        return a
    if s==e:
        return av*b
    p=check(s,(s+e)//2)+check(((s+e)//2)+1,e)
    cp=av*b*(e-s+1)
    return min(cp,p)

n,k,a,b=map(int,input().split())
h=list(map(int,input().split()))
h.sort()
n=2**n
res=check(1,n)
print(res)