t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    s=False
    for i in range(1,n):
        if a[i]<a[i-1]:
            s=True
            break
    if s==True or n==1:
        print(1)
    else:
        print(n)
