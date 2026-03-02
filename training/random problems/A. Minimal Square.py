t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    x=max(n,m)
    y=min(n,m)
    if x>y*2:
        print(x*x)
    else:
        print((y*2)*(y*2))