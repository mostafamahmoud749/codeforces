t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    d6=[]
    d2=[]
    d3=[]
    ne=[]
    for i in a:
        if i%6==0:
            d6.append(i)
        elif i%2==0:
            d2.append(i)
        elif i%3==0:
            d3.append(i)
        else:
            ne.append(i)
    res=d6+d2+ne+d3
    print(*res)