t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    l=list(map(int,input().split()))
    new_a=[]
    l_=[]
    for i in range(n):
        if l[i]==0:
            new_a.append(a[i])
        else:
            l_.append((a[i],i))
    new_a.sort(reverse=True)
    for i in range(len(l_)):
        new_a.insert(l_[i][1],l_[i][0])
    
    print(*new_a)