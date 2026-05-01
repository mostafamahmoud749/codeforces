t=int(input())
for _ in range(t):
    n,j,k=map(int,input().split())
    a=list(map(int,input().split()))
    el=a[j-1]
    if max(a)==el or k>=2:
        print("YES")
    else:
        print("NO")