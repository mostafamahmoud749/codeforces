t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    x=a[0]
    for i in range(1,n):
        x^=a[i]
    if (n&1)==1:
        print(x)
    else:
        if x==0:
            print(0)
        else: 
            print(-1)