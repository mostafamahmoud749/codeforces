t=int(input())
for k in range(t):
    n=int(input())
    count=0
    p=0
    if n<2020:
        print("NO")
        continue
    while n>0:
        n-=2020
        count+=1
        p=n+2020
    if count>=p:
        print("YES")
    else:
        print("NO")