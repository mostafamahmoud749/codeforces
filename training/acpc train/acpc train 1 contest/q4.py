t=int(input())
for _ in range(t):
    n=int(input())
    bits=bin(n)
    i=len(bits)-1
    res=1
    while i>1 and bits[i]!="1":
        if bits[i]=="0":
            res+=1
        i-=1
    print(res)
