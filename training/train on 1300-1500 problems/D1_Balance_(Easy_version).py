q=int(input())
s=set()
s.add(0)
k={}
for _ in range(q):
    t,x=input().split()
    x=int(x)
    if t=="+":
        s.add(x)
    else:
        if x not in k:
            k[x]=x
        while k[x] in s:
            k[x]+=x
        print(k[x])
