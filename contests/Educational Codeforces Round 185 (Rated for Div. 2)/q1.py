t=int(input())
for _ in range(t):
    n=int(input())
    if n==1:
        print(1)
    else:
        res=0
        for i in range(n):
            for j in range(n):
                v = i*n+j+1
                c=v
                if i > 0: c += v - n
                if i < n - 1: c += v + n
                if j > 0: c += v - 1
                if j < n - 1: c += v + 1
                if c > res:
                    res=c
        print(res)