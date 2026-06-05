t=int(input())
for _ in range(t):
    n=input()
    s=False
    for i in range(1,len(n)):
        if 65<=ord(n[i])<=90 and not (65<=ord(n[i-1])<=90):
            s=True
            break
    if s:
        cindx=n.index("C")
        rv=n[1:cindx]
        cv=int(n[cindx+1:])
        cr=[]
        while cv>0:
            rem=cv%26
            if rem==0:
                rem=26
                cv=(cv//26)-1
            else:
                cv=cv//26
            cr.append(chr(64+rem))
        cr=cr[::-1]
        print("".join(cr)+rv)
    else:
        s=-1
        for i in range(len(n)):
            if not 65<=ord(n[i])<=90:
                s=i
                break
        cc=n[:i]
        rv=n[i:]
        cv=0
        for i in range(len(cc)):
            cv=(26*cv)+(ord(cc[i])-64)
        print("R"+str(rv)+"C"+str(cv))