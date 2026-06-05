t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=list(input().strip())
    st=True
    for i in range(k,n):
        if s[i]!="?":
            if s[i%k]=="?":
                s[i%k]=s[i]
            elif s[i%k]!=s[i]:
                st=False
                break
    c1=s[:k].count("1")
    c0=s[:k].count("0")
    cq=s[:k].count("?")
    cq-=abs(c1-c0)
    print("NO") if (not st or cq<0 or cq%2!=0) else print("YES")
