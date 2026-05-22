def genrate(c,cn,cs):
    global n
    ncs=cs.copy()
    if len(c)==len(s):
        p.add(c)
    if len(c)<len(s)//2 and cn<n and cn>(len(s)//2)-len(c):
        return
    if len(c)==len(s)//2 and cn!=n and cn!=0:
        return
    for i in range(len(cs)):
        new_c=c+cs[i]
        new_cn=cn
        if cs[i]==cx or cs[i]==cy:
            new_cn=-1
        ncs=cs[:i]+cs[i+1:]
        genrate(new_c,new_cn,ncs)

s=list(input().strip())
q=int(input())
letters=set(s)
for i in range(q):
    x,y=map(int,input().split())
    cx = s[x-1]
    cy = s[y-1]
    n=s.count(cx)+s.count(cy)
    if n>len(s)//2:
        print(0)
    else:
        p=set()
        genrate("",n,s)
        print(len(p))