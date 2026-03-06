n,m=map(int,input().split())
if m%n!=0:
    print(-1)
else:
    count=0
    q=m/n
    while q%2==0:
        count+=1
        q=q/2
    while q%3==0:
        count+=1
        q=q/3
    if q==1:
        print(count)
    else:
        print(-1)