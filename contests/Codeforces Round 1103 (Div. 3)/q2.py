t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(input().strip())
    for i in range(n-k):
        if a[i]=="1":
            a[i]="0"
            if a[i+k]=="1":
                a[i+k]="0"
            else:
                a[i+k]="1"
    print("YES") if a.count("1")==0 else print("NO")