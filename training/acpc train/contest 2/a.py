t=int(input())
for _ in range(t):
    n=input()
    out=[]
    for i in range(len(n)):
        if n[i]!="0":
            out.append(n[i]+("0"*(len(n)-i-1)))
    print(len(out))
    print(*out)