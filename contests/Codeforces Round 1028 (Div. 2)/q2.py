t=int(input())
for _ in range(t):
    n=int(input())
    p=list(map(int,input().split()))
    q=list(map(int,input().split()))
    r=[]
    for i in range(n):
        b=(-1,-1)
        for j in range(i+1):
            x=p[j]
            y=q[i-j]
            cur_b=(max(x,y),min(x,y))
            if cur_b>b:
                b=cur_b
        r.append(((2**(b[0])%998244353)+(2**(b[1]))%998244353)%998244353)
    print(*r)