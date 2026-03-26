t=int(input())
for _ in range(t):
    n,c,k=map(int,input().split())
    a=sorted(map(int,input().split()))
    print(a)
    for i in a:
        if i > c:
            break
        e=min(k,c-i)
        c+=i+e
        k-=e
    print(c)