t=int(input())
for _ in range(t):
    n=int(input())
    afreq=[0]*26
    bfreq=[0]*26
    afreq[0]=1
    bfreq[0]=1
    for i in range(n):
        p=input().split()
        op=int(p[0])
        x=p[1]
        k=int(p[2])
        if op==1:
            for ch in x:
                c=ord(ch)
                afreq[c-97]+=k
        else:
            for ch in x:
                c=ord(ch)
                bfreq[c-97]+=k
        s=False
        for j in range(26):
            if afreq[j]>bfreq[j]:
                s=True
                if sum(bfreq[j+1:])>0:
                    print("Alice")
                else:
                    print("Bob")
                break
            elif afreq[j]<bfreq[j]:
                s=True
                if sum(afreq[j+1:])>0:
                    print("Bob")
                else:
                    print("Alice")
                break
        if s==False:
            print("Tie")