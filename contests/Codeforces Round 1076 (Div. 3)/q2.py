t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    saved=-1
    saved_indx=-1
    for i in range(n):
        if a[i]!=n-i and saved==-1:
            saved=n-i
            saved_indx=i
        elif a[i]==saved:
            a[saved_indx:i+1] = reversed(a[saved_indx:i+1])
            break
    print(*a)
