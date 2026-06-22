t=int(input())
for _ in range(t):
    n=int(input())
    if n<=2:
        print(0)
        continue
    res=[]
    for i in range(1,n):
        if i%2==0:
            res.append("B")
        else:
            res.append("F")
    res[-1]="B"
    print(n-1)
    print("".join(res))
    
