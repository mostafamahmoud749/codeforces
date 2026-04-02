import math
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    db=[-1]*1001
    for i in range(n):
        db[a[i]]=i+1
        
    summ=-1
    for i in range(1,1001):
        if db[i]!=-1:
            for j in range(i, 1001):
                if db[j]!=-1 and math.gcd(i, j) == 1:
                    summ=max(summ, db[i] + db[j])
    print(summ)