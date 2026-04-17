t=int(input())
for i in range(t):
    n=int(input())
    a=[0]*n
    a[0] = (n-1)//2 + 1
    for i in range(1,n):
        if i % 2 == 1:
            a[i]=a[i-1]+i
        else:
            a[i]=a[i-1]-i
    print(*a)