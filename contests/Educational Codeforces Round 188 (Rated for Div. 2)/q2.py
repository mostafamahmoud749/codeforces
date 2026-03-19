t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    new_a=[]
    for i in range(n):
        new_a.append((a[i],i))
    new_a.sort(key=lambda x: (x[0], x[1]), reverse=True)
    res=0
    del_indx=float("inf")
    for i in range(n):
        if new_a[i][1]<del_indx:
            res+=1
            del_indx=new_a[i][1]
    print(res)