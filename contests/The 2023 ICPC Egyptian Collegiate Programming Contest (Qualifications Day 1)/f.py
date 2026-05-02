t=int(input())
for _ in range(t):
    s=input()
    while not s:
        s=input()
    t=input()
    while not t:
        t=input()
    c=0
    i=0
    while i<=len(s)-len(t):
        if s[i:i+len(t)]==t:
            c+=1
            s=s[:i]+s[i+len(t):]
            i=max(0,i-len(t))
        else:
            i+=1
    print(c)