t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    sr=a.index(b[0])
    if sr==0:
        indx=0
        for i in range(n):
            if a[i]==b[i]:
                continue
            else:
                indx=i
                break
        for i in range(indx,n):
            if a[i]!=b[i]:
                print("NO")
                break
        else:
            print("YES")
    else:
        s=True
        for i in range(sr,n):
            if a[i]!=b[i-sr]:
                print("NO")
                s=False
                break
        if s==True:
            for i in range(0,sr):
                if a[i]!=b[i+(n-sr)]:
                    print("NO")
                    break
            else:
                print("YES")