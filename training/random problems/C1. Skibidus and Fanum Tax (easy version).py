t=int(input())
for j in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=int(input())
    x=-1
    posiple=True
    for k in range(n):
        curent=min(a[k],b-a[k])
        if curent < x:
            posiple = False
            break
        x=curent
    if posiple:
        print("YES")
    else:
        print("NO")