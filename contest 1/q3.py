t=int(input())
for _ in range(t):
    n=int(input())
    num=input().strip()
    a=[]
    for i in range(len(num)):
        if int(num[i])%2!=0:
            a.append(num[i])
        if len(a)==2:
            break
    if len(a)==2:
        print(a[0]+a[1])
    else:
        print(-1)