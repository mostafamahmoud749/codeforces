t=int(input())
for _ in range(t):
    n,x1,x2,k=map(int,input().split())
    rem=abs(x2-x1)
    a=min(rem,n-rem)
    if n<=3:
        res=1
    else:
        res=a+k
    print(res)