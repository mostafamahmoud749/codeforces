t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    p=[0]*31
    res=0
    for i in a:
        res+=p[i.bit_length()-1]
        p[i.bit_length()-1]+=1
    print(res)
