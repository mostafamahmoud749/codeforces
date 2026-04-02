
t=int(input())
for _ in range(t):
    n=int(input())
    res=0
    while n>0:
        m = 0
        p = 1
        while p*3<=n:
            p*=3
            m+=1
        if m == 0:
            res += 3
        else:
            res += (3**(m+1)) + (m*(3**(m-1)))
        n -= p
    print(res)
