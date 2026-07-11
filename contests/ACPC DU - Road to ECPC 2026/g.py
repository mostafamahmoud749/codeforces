t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    s=True
    for i in range(1,n):
        if a[i]<=a[i-1]:
            s=False
            break
    print("Yes") if s else print("No")