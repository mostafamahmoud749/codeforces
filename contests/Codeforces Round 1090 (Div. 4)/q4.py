import math
t=int(input())
for _ in range(t):
    n=int(input())
    res=[1]
    s=set()
    i=2
    while len(res)<n:
        v=math.gcd(res[-1],i*(i-1))
        if v not in s:
            res.append(i*(i-1))
            s.add(v)
        i+=1
    print(*res)