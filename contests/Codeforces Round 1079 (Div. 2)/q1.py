t=int(input())
for _ in range(t):
    n=int(input())
    s = False
    for y in range(n, n + 91):
        if y-sum(int(d) for d in str(y)) == n:
            s=True
            break
    print(10) if s else print(0)
