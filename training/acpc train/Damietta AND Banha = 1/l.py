t=int(input())
for _ in range(t):
    q,m=map(int,input().split())
    p=[0]*1500
    s=True
    for _ in range(q):
        l,r=map(str,input().split())
        r=int(r)
        if s:
            l=(int(l[0:2])*60)+int(l[3:])
            if l+r>1440:
                continue
            for i in range(l,l+r):
                p[i]+=1
                if p[i]>m:
                    s=False
                    break
    print("YES") if s else print("NO")
