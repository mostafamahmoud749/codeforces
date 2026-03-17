t=int(input())
for _ in range(t):
    n=int(input())
    m=list(map(int,input().split()))
    db={}
    max_c=(n-1)*n
    tt=True
    if n==1:
        print("YES")
        continue

    for i in range(n-1):
        n_m=list(map(int,input().split()))
        m.extend(n_m)
    for i in range(n*n):
        if m[i] in db:
            db[m[i]]+=1
            if db[m[i]]>max_c:
                tt=False
                break
        else:
            db[m[i]]=1

    if tt==True:
        print("YES")
    else:
        print("NO")

