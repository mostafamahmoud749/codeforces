t=int(input())
for _ in range(t):
    s=list(input().strip())
    res=0
    c13=0
    for i in range(len(s)):
        if s[i]=="4":
            res+=1
        elif s[i]=="1" or s[i]=="3":
            c13+=1
        else:
            if c13>0:
                res+=1
                c13-=1
    print(res)