t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    res=0
    for k in range((n//2)+1):
        s=set()
        stat=False
        p=[]
        i=0
        j=0
        while i<n:
            while a[i] in s:
                s.remove(a[j])
                j+=1
            s.add(a[i])
            i+=1
            if len(s)==k:
                maxa=max(a[j:i])
                mina=min(a[j:i])
                if maxa-mina==k-1:
                    p.append([j,i-1,mina,maxa])
                s.remove(a[j])
                j+=1
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                if p[i][1]<p[j][0] or p[j][1]<p[i][0]:
                    if p[i][3]+1==p[j][2] or p[j][3]+1==p[i][2]:
                        stat=True
                        break
            if stat:
                break
        if stat:
            res=k
    print(res)
