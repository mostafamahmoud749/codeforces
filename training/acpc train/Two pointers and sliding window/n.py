t=int(input())
for _ in range(t):
    s=input()
    res=0
    for i in range(len(s)//2,0,-1):
        if i*2 <= res:
            break
        c=0
        for j in range(len(s)-i):
            if s[j] == s[i+j] or s[j] == "?" or s[i+j] == "?":
                c+=1
            else:
                c=0
            if c==i:
                res=max(res,i*2)
                break
    print(res)
