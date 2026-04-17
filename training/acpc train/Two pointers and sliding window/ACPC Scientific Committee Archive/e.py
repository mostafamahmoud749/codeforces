n,w=map(int,input().split())
a=list(map(int,input().split()))
e=[]
o=[]
for i in range(n):
    if a[i]%2==0:
        e.append(a[i])
    else:
        o.append(a[i])
e=set(e)
e=list(e)
p=set([0])
for i in o:
    c=list(p)
    for j in c:
        if i+j<=w:
            p.add(i+j)
for i in range(len(e)):
    v=w-e[i]
    if v in p:
        print("YES")
        break
else:
    print("NO")