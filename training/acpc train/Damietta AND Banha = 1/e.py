t=int(input())
for _ in range(t):
    n=int(input())
    res=0
    for i in range(n.bit_length()):
        if (n>>i)&1==0:
            res+=2**i
    print(res)