t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    total=n+m
    res=0
    d=""
    fr=-1
    l=-1
    taken=[]
    out=[]
    for i in range(total):
        if n>0 and m>0:
            if a[i]>b[i]:
                res+=a[i]
                n-=1
                taken.append("a")
                if n==0:
                    l=i
            else:
                res+=b[i]
                m-=1
                taken.append("b")
                if m==0:
                    l=i
        elif m==0:
            res+=a[i]
            taken.append("a")
            if fr==-1 and b[i]>a[i]:
                fr=i
                d="m"
        else:
            res+=b[i]
            taken.append("b")
            if fr==-1 and a[i]>b[i]:
                fr=i
                d="n"
    for i in range(total+1):
        if i==total:
            out.append(res)
        elif taken[i]=="a":
            if d=="n" and l>=i:
                out.append(res-a[i]+(a[fr]-b[fr])+b[total])
            else:
                out.append(res-a[i]+a[total])
        else:
            if d=="m" and l>=i:
                out.append(res-b[i]+(b[fr]-a[fr])+a[total])
            else:
                out.append(res-b[i]+b[total])
    print(*out)