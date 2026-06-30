t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    p=[0]*(n+1)

    for i in range(1,n+1):
        p[i]=p[i-1]^a[i-1]

    if p[-1]==0:
        print("YES")
        continue

    s=False
    for i in range(1,n):
        for j in range(i+1,n):
            if p[i]==(p[j]^p[i])==(p[-1]^p[j]):
                s=True
                break
        if s:
            break

    print("YES") if s else print("NO")