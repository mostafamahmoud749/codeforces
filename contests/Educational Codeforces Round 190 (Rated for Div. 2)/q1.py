t=int(input())
for _ in range(t):
    n,a,b=map(int,input().split())
    res=0
    if b/3<a:
        res+=(n//3)*b
        n=n%3
        if a*n<b:
            res+=a*n
        else:
            res+=b
    else:
        res+=n*a
    print(res)