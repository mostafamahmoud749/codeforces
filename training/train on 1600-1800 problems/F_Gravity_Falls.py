t=int(input())
for _ in range(t):
    n=int(input())
    a=[]
    for i in range(n):
        a.append(list(map(int,input().split()))[1:])
    a.sort(key=len)
    res=[float("inf")]*len(a[-1])
    e=[0]
    for i in range(n):
        la=len(a[i])
        for j in range(len(e)):
            s=False
            l=e[j]
            if l>=la: continue
            if j!=len(e)-1:
                r=min(e[j+1],la)
            else:
                r=la
            for k in range(l,r):
                if res[k]<a[i][k]: break
                if res[k]>a[i][k]: 
                    s=True 
                    break
            if s:
                for k in range(l,la):
                    res[k]=a[i][k]
                while e[-1]>l: e.pop()
                e.append(la)
                break
    print(*res)
    